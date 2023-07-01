import cocotb

from cocotb.triggers import Timer, FallingEdge, RisingEdge, ReadOnly, NextTimeStep

from cocotb_bus.drivers import BusDriver

from cocotb_bus.monitors import BusMonitor

from cocotb_coverage.coverage import CoverCross, CoverPoint, coverage_db

import os

import random

@CoverPoint(f"top.pres_state",  # noqa F405

            xf=lambda x: x['current'],

            bins=['Idle', 'SETUP', 'ACESS'],

            )

@CoverPoint(f"top.prev_state",  # noqa F405

            xf=lambda x: x['previous'],

            bins=['Idle', 'SETUP', 'ACESS'],

            )

@CoverCross("top.cross",

            items=[

                "top.prev_state", "top.pres_state"

            ]

            )

def state_cover(state):

    cocotb.log.warning(f"state={state}")

    pass

@cocotb.test()

async def master1(master):

    #RESET#

    master.PRESETn.value = 1

    await Timer(1, 'ns')

    master.PRESETn.value = 0

    await Timer(1, 'ns')

    await RisingEdge(master.PCLK)

    master.PRESETn.value = 1

    master.apb_write_paddr.value=10
    
    await RisingEdge(master.PCLK)

    master.apb_write_data=28

    await RisingEdge(master.PCLK)

    p_drv=InputDriver(master,'',master.PCLK)

    InputMonitor(master, '',master.PCLK, callback=state_cover)

    master.transfer.value=1

    master.READ_WRITE.value=0

    for i in range(10):
        master.apb_write_data=28+i
        await Timer(1,'ns')
        master.apb_write_paddr.value=10+i
        await Timer(3,'ns')
        await RisingEdge(master.PCLK)


    coverage_db.report_coverage(cocotb.log.info, bins=True)

    coverage_file = os.path.join(

        os.getenv('RESULT_PATH', "./"), 'coverage.xml')

    coverage_db.export_to_xml(filename=coverage_file)
        
    
    await ReadOnly()
    await Timer(3,'ns')


#read data from slave to master


@cocotb.test()

async def slave1(master):

    #RESET#

    master.PRESETn.value = 1

    await Timer(1, 'ns')

    master.PRESETn.value = 0

    await Timer(1, 'ns')

    await RisingEdge(master.PCLK)

    master.PRESETn.value = 1

    master.apb_read_paddr.value=101
    
    await RisingEdge(master.PCLK)

    p_drv=InputDriver(master,'',master.PCLK)

    InputMonitor(master, '',master.PCLK, callback=state_cover)

    master.transfer.value=1

    master.READ_WRITE.value=1

    for i in range(10):
        master.PRDATA.value=28+i
        await Timer(4,'ns')
        await RisingEdge(master.PCLK)    

    
    coverage_db.report_coverage(cocotb.log.info, bins=True)

    coverage_file = os.path.join(

        os.getenv('RESULT_PATH', "./"), 'coverage1.xml')

    coverage_db.export_to_xml(filename=coverage_file)    
    await ReadOnly()
    await RisingEdge(master.PCLK)    

#driver 
class InputDriver(BusDriver):

    _signals=['PREADY','PENABLE']

    def __init__(self,dut,name,clk):

        BusDriver.__init__(self,dut,name,clk)

        self.bus.PREADY.value=0

        self.clk=clk
        self.append(0)



    async def _driver_send(self,value,sync=True):

        while True:

            if self.bus.PENABLE.value !=1 :

                await RisingEdge(self.bus.PENABLE)

            self.bus.PREADY.value=1

            await RisingEdge(self.clk)

            self.bus.PREADY.value=0

            await ReadOnly()

            await NextTimeStep()
#IO_moniter

class InputMonitor(BusMonitor):

    _signals = ['PENABLE', 'PSEL1']

    


    async def _monitor_recv(self):
        await Timer(2,'ns') 


        fallingedge = FallingEdge(self.clock)

        rdonly = ReadOnly()

        prev_state = 'Idle'

        state = {

            0: 'Idle',

            1: 'SETUP',

            3: "ACESS"

        }

        while True:

            await fallingedge

            await rdonly

            s = state[self.bus.PENABLE.value << 1| (self.bus.PSEL1.value)]

            self._recv({'current': s, 'previous': prev_state})

            prev_state = s 
            await Timer(2,'ns')      
