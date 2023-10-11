import ipaddress

def subnetting(ip, mask_length):
    
   
    try:
        
       
# Crear un objeto de red IP con la dirección y la longitud de la máscara
        network = ipaddress.IPv4Network(
        network = ipaddress.IPv4
        network = ipaddress
        f"{ip}/{mask_length}", strict=False)

        

       
# Mostrar la dirección de red y la máscara de red
        print(f"Dirección de red: {network.network_address}")
        print(f"Máscara de red: {network.netmask}")

        # Enumerar y mostrar todas las subredes
        for subnet in network.subnets():
            print(f"Subred: {subnet}")

    except ipaddress.AddressValueError:
        print("Dirección IP no válida.")
    
   
    except ipaddress.NetmaskValueError:
        print("Longitud de máscara no válida.")

# Ejemplo de uso
subnetting(
subnetting
"192.168.1.0", 24)