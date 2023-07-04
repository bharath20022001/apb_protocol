# APB-Protocol

  # Intro
APB is low bandwidth and low performance bus. So, the components requiring lower bandwidth like the peripheral devices such as UART, Keypad, Timer and PIO (Peripheral Input Output) devices are connected to the APB.
The bridge connects the high performance AHB or ASB bus to the APB bus. So, for APB the bridge acts as the master and all the devices connected on the APB bus acts as the slave.


# APB Specification
1. Parallel bus operation. All the data will be captured at rising edge clock.
2. Two slave design.
3. Signal priority: 1.PRESET (active low) 2. PSEL (active high) 3. PENABLE (active high) 4. PREADY (active high) 5. PWRITE 
4. Data width 8 bit and address width 9 bit. 
5. PWRITE=1 indicates write PWDATA to slave.
   PWRITE=0 indicates read PRDATA from slave.
6. Start of data transmission is indicated when PENABLE changes from low to high. End of transmission is indicated by PREADY changes from high to low.


Top Module Name: apb_protocol.v
Testbench Name: master_txtb.v
Testbench Name: master_rxtb.v

Operation Of APB

![image](https://user-images.githubusercontent.com/82434808/122651071-1681de80-d154-11eb-9977-9d46bacd77b9.png)



APB PIN Description:

<meta name="ProgId" content="PowerPoint.Slide">
<meta name="Generator" content="Microsoft PowerPoint 15">
<style>
<!--tr
	{mso-height-source:auto;}
col
	{mso-width-source:auto;}
td
	{padding-top:1.0px;
	padding-right:1.0px;
	padding-left:1.0px;
	mso-ignore:padding;
	color:windowtext;
	font-size:18.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Arial;
	mso-generic-font-family:auto;
	mso-font-charset:0;
	text-align:general;
	vertical-align:bottom;
	border:none;
	mso-background-source:auto;
	mso-pattern:auto;}
.oa1
	{border:1.0pt solid black;
	background:white;
	mso-pattern:auto none;
	text-align:center;
	vertical-align:top;
	padding-bottom:3.6pt;
	padding-left:7.2pt;
	padding-top:3.6pt;
	padding-right:7.2pt;}
.oa2
	{border:1.0pt solid black;
	background:white;
	mso-pattern:auto none;
	vertical-align:top;
	padding-bottom:3.6pt;
	padding-left:7.2pt;
	padding-top:3.6pt;
	padding-right:7.2pt;}
-->
</style>



<!--StartFragment-->


SIGNAL | SOURCE | Description | WIDTH(Bit)
-- | -- | -- | --
Transfer | System Bus | APB enable signal. If high APB is   activated else APB is disabled | 1
PCLK | Clock Source | All APB functionality occurs at a rising edge. | 1
PRESETn | System Bus | An active low signal. | 1
PADDR | APB bridge | The APB address bus can be up to 32   bits. | 8
PSEL1 | APB bridge | There is a PSEL for each slave. It’s an active high signal. | 1
PENABLE | APB bridge | It indicates the 2nd cycle of a data transfer. It’s an active high signal. | 1
PWRITE | APB bridge | Indicates the data transfer direction.   PWRITE=1 indicates APB write   access(Master to slave)    PWRITE=0 indicates APB read   access(Slave to master) | 1
PREADY | Slave Interface | This is an input from Slave. It is used to enter the access state. | 1
PSLVERR | Slave Interface | This indicates a transfer failure by the slave. | 1
PRDATA | Slave Interface | Read Data. The selected slave drives   this bus during reading operation | 8
PWDATA | Slave Interface | Write data. This bus is driven by the peripheral bus bridge unit during write cycles when PWRITE is high. | 8


# Test bench

The test bench was writen by using <a href = "https://www.cocotb.org/" >cocotb</a> framework. All states has been covered when data is transmitting and receiving from master.

The test bench for transmitting data from master is written in <a href = "https://github.com/Bharathreddy02/apb_protocal/blob/main/tests/master_txtb.py" >master_txtb.py</a>

The test bench for receiving data from master is written in <a href = "https://github.com/Bharathreddy02/apb_protocal/blob/main/tests/master_rxtb.py" >master_rxtb.py</a>

master transmission waveform
![image](https://github.com/Bharathreddy02/apb_protocal/assets/135442130/c4ee443c-981a-451f-bac6-0187ef9c7730)

master receiving waveform

![image]([https://github.com/Bharathreddy02/apb_protocal/blob/main/tests/waves/rx.png](https://github.com/Bharathreddy02/apb_protocal/assets/135442130/12e7bd2f-7c60-4b3a-bdd0-deb79432a364)https://github.com/Bharathreddy02/apb_protocal/assets/135442130/12e7bd2f-7c60-4b3a-bdd0-deb79432a364)




