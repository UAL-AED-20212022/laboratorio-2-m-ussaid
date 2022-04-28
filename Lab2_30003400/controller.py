from model.LinkedList import LinkedList

# Registar país no início
def RPI(linkedList, new_pais):
    linkedList.insert_at_start(new_pais)
    linkedList.traverse_list()
    return

# Registar país no final
def RPF(linkedList, new_pais):
    linkedList.insert_at_end(new_pais)
    linkedList.traverse_list()
    return 

# Registar país depois de um outro país já registado
def RPDE(linkedList, new_pais, pais_registado):
    linkedList.insert_after_item(pais_registado, new_pais)
    linkedList.traverse_list()
    return

# Registar país antes de um outro elemento já registado
def RPAE(linkedList, new_pais, pais_registado):
    linkedList.insert_before_item (pais_registado, new_pais)
    linkedList.traverse_list()
    return

# Registar país num índice especificado
def RPII(linkedList, new_pais, index: int):
    linkedList.insert_at_index(index, new_pais)
    linkedList.traverse_list()
    return

# Verificar o número de elementos da lista
def VNE(linkedList):
    print(f"O número de elementos são {linkedList.get_count()}")
    return

# Verificar se um país se encontra na lista
def VP(linkedList, pais_name):
    if (linkedList.search_item(pais_name) == True):
        print(f"O país {pais_name} encontra-se na lista")
        return

    elif (linkedList.search_item(pais_name) == False):
        print(f"O país {pais_name} não se encontra na lista")
        return

# Eliminar o primeiro elemento da lista
def EPE(linkedList):

    pais = linkedList.start_node.item
    linkedList.delete_at_start()
    print(f"O país {pais} foi eliminado da lista")
    return

# Eliminar o último elemento da lista
def EUE(linkedList):

    pais = linkedList.get_last_node()
    linkedList.delete_at_end()
    print(f"O país {pais} foi eliminado da lista")
    return

# Eliminar um determinado país da lista
def EP(linkedList, pais_name):

    if (linkedList.search_item(pais_name) == True):
        linkedList.delete_element_by_value(pais_name)
        print(f"O país {pais_name} foi eliminado da lista")
        return

    elif (linkedList.search_item(pais_name) == False):
        print(f"O país {pais_name} não se encontra na lista")
        return