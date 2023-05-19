from var_voltage_control.voltage_barrier.bowl import bowl
from var_voltage_control.voltage_barrier.bump import bump
from var_voltage_control.voltage_barrier.courant_beltrami import courant_beltrami
from var_voltage_control.voltage_barrier.l1 import l1
from var_voltage_control.voltage_barrier.l2 import l2



Voltage_Barrier = dict(
    l1=l1,
    l2=l2,
    bowl=bowl,
    bump=bump,
    courant_beltrami=courant_beltrami
)