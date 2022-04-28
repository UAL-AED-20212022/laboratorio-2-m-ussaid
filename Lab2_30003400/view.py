import controller as ctrl
from model.LinkedList import LinkedList

linkedList = LinkedList()

def main():

    while True:
        command = input().split()

        if command[0] == "RPI":
            new_pais = command[1]
            ctrl.RPI(linkedList, new_pais)

        elif command[0] == "RPF":
            new_pais = command[1]
            ctrl.RPF(linkedList, new_pais)

        elif command[0] == "RPDE":               
            new_pais = command[1]
            pais_registado = command[2]
            ctrl.RPDE(linkedList, new_pais, pais_registado)

        elif command[0] == "RPAE":
            new_pais = command[1]
            pais_registado = command[2]
            ctrl.RPAE(linkedList, new_pais, pais_registado)

        elif command[0] == "RPII":
            new_pais = command[1]
            index = int(command[2])
            ctrl.RPII(linkedList, new_pais, index)

        elif command[0] == "VNE":
            ctrl.VNE(linkedList)
 
        elif command[0] == "VP":
            pais_name = command[1]
            ctrl.VP(linkedList, pais_name)

        elif command[0] == "EPE":
            ctrl.EPE(linkedList)

        elif command[0] == "EUE":
            ctrl.EUE(linkedList)

        elif command[0] == "EP":
            pais_name = command[1]
            ctrl.EP(linkedList, pais_name)