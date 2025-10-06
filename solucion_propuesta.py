class RegisterAllocator:
    def __init__(self):

        self.registers = {}
        self.registers["R1"] = None
        self.registers["R2"] = None
        self.registers["R3"] = None
        self.memory = {}

    def get_register(self, variable):

        registro_encontrado = None
        lista_de_registros = list(self.registers.keys())

        indice = 0
        while indice < len(lista_de_registros):
            nombre_registro = lista_de_registros[indice]
            contenido = self.registers[nombre_registro]
            if contenido == variable:
                registro_encontrado = nombre_registro
                break
            indice = indice + 1

        if registro_encontrado is not None:
            return registro_encontrado

        indice = 0
        while indice < len(lista_de_registros):
            nombre_registro = lista_de_registros[indice]
            contenido = self.registers[nombre_registro]
            if contenido is None:
                self.registers[nombre_registro] = variable
                return nombre_registro
            indice = indice + 1

        resultado_spilling = self.spill_and_assign(variable)
        return resultado_spilling

    def spill_and_assign(self, variable):
        lista_de_registros = list(self.registers.keys())
        indice = 0

        while indice < len(lista_de_registros):
            nombre_registro = lista_de_registros[indice]
            contenido = self.registers[nombre_registro]

            if contenido is not None:
                self.memory[contenido] = "Spilled from " + nombre_registro
                self.registers[nombre_registro] = variable
                return nombre_registro

            indice = indice + 1

        return "ERROR: No se pudo asignar registro"

    def __str__(self):

        texto = "Estado actual:\n"
        texto = texto + "Registros:\n"

        lista_de_registros = list(self.registers.keys())
        indice = 0
        while indice < len(lista_de_registros):
            nombre_registro = lista_de_registros[indice]
            contenido = self.registers[nombre_registro]
            texto = texto + "  " + nombre_registro + ": " + str(contenido) + "\n"
            indice = indice + 1

        texto = texto + "Memoria (Spilled):\n"
        lista_de_variables = list(self.memory.keys())
        j = 0
        while j < len(lista_de_variables):
            nombre_variable = lista_de_variables[j]
            origen = self.memory[nombre_variable]
            texto = texto + "  " + nombre_variable + ": " + origen + "\n"
            j = j + 1

        return texto
asignador = RegisterAllocator()

print(asignador.get_register("a"))  
print(asignador.get_register("b"))  
print(asignador.get_register("c"))  
print(asignador.get_register("d")) 

print(asignador)