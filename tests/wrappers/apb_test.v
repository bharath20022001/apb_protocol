`timescale 1ns/1ns

 module master_test(
	input [8:0]apb_write_paddr,apb_read_paddr,
	input [7:0] apb_write_data,PRDATA,         
	input PRESETn,READ_WRITE,transfer,PREADY,
	output reg PCLK,
	output PSEL1,PSEL2,
	output reg PENABLE,
	output reg [8:0]PADDR,
	output reg PWRITE,
	output reg [7:0]PWDATA,apb_read_data_out,
	output PSLVERR ); 

master_bridge mas(
	.apb_write_paddr(apb_write_paddr),
	.apb_read_paddr(apb_read_paddr),
	.apb_write_data(apb_write_data),
	.PRDATA(PRDATA),
	.PRESETn(PRESETn),
	.PCLK(PCLK),
	.READ_WRITE(READ_WRITE),
	.transfer(transfer),
	.PREADY(PREADY),
	.PSEL1(PSEL1),
	.PSEL2(PSEL2),
	.PENABLE(PENABLE),
	.PADDR(PADDR),
	.PWRITE(PWRITE),
	.PWDATA(PWDATA),
	.apb_read_data_out(apb_read_data_out),
	.PSLVERR(PSLVERR)
);
initial begin
	$dumpfile("master.vcd");
	$dumpvars;
	PCLK=0;
	forever begin
            #1 PCLK=~PCLK;
        end
end
endmodule
