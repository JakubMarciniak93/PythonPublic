PL
Wersia 0.5.0
Jest to prosty symulator interface'u pralki.
Jego zadaniem jest zasymulowanie działania pralki,
podłączenie się do urządzenia zawnętrzenego, kótre
może byc jednostką sterującą całego urządzenia i 
sterować podzespołami np. silnikiem czy systemem 
odprowadzania wody czy podawania detergentów.

Obecny stan:
Symulator pozwala na połączenie się z urządzenie zewnętrznym
za pomocą protokołu ssh. Obecnie symulujemy jedynie czas, 
zapisujemy stan w logach i przeprowadzamy proste połączenie
z urządzeniem zewnętrzym posiadającym system linux. 

ENG
Version 0.5.0
This is a simple washing machine interface simulator.
Its task is to simulate the operation of the washing machine,
connecting to an external device that
can be the control unit of the entire device i
control components, e.g. an engine or a system
draining water or feeding detergents.

Current state:
The simulator allows you to connect to an external device
using the ssh protocol. Currently, we only simulate time,
we save the status in the logs and make a simple connection
with an external device running Linux.