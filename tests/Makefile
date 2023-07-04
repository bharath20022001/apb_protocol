SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/master.v
VERILOG_SOURCES += $(PWD)/../tests/wrappers/apb_test.v
VERILOG_SOURCES += $(PWD)/../hdl/slave1.v
VERILOG_SOURCES += $(PWD)/../hdl/slave2.v
apb_rx:
	rm -rf sim_build
	$(MAKE) sim MODULE=master_rxtb TOPLEVEL=master_test
apb_tx:
	rm -rf sim_build
	$(MAKE) sim MODULE=master_txtb TOPLEVEL=master_test		
							
include $(shell cocotb-config --makefiles)/Makefile.sim
