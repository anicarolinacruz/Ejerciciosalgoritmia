<<<<<<< HEAD
import clase
#creando objeto
persona= clase.Persona()
persona.setNombre("Sandra")
persona.setApellidos("Cruz")
persona.setAltura("1.68")
persona.setEdad("42")
print(f"La persona: {persona.getNombre()}{persona.getApellidos()} {persona.getAltura()} {persona.getEdad()}")
print(persona.hablar())
print(persona.caminar())
print(persona.dormir())
print("------------------------------")
print("AQUI EMPIEZA LA SUBCLASE INFORMATICO")
#Creando objeto
informatico=clase.Informatico()
informatico.setNombre("Stefy")
informatico.setApellidos("Martinez")
print(f"El informático: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print("------------------------------")
print("AQUI EMPIEZA LA SUBCLASE TECNICOREDES HIJO DE INFORMATICO")
#creando objeto
tecnico=clase.TecnicoRedes()
tecnico.setNombre("Jhon")
print(f"Nivel de autoria:{tecnico.getAuditoriaredes()},{tecnico.getNombre()},lenguajes:{tecnico.getLenguajes()},Audita:{tecnico.auditar()},Experiencia:{tecnico.getExperienciaredes()}")
=======
import clase
#creando objeto
persona= clase.Persona()
persona.setNombre("Sandra")
persona.setApellidos("Cruz")
persona.setAltura("1.68")
persona.setEdad("42")
print(f"La persona: {persona.getNombre()}{persona.getApellidos()} {persona.getAltura()} {persona.getEdad()}")
print(persona.hablar())
print(persona.caminar())
print(persona.dormir())
print("------------------------------")
print("AQUI EMPIEZA LA SUBCLASE INFORMATICO")
#Creando objeto
informatico=clase.Informatico()
informatico.setNombre("Stefy")
informatico.setApellidos("Martinez")
print(f"El informático: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print("------------------------------")
print("AQUI EMPIEZA LA SUBCLASE TECNICOREDES HIJO DE INFORMATICO")
#creando objeto
tecnico=clase.TecnicoRedes()
tecnico.setNombre("Jhon")
print(f"Nivel de autoria:{tecnico.getAuditoriaredes()},{tecnico.getNombre()},lenguajes:{tecnico.getLenguajes()},Audita:{tecnico.auditar()},Experiencia:{tecnico.getExperienciaredes()}")
>>>>>>> 9df5d5dc0c2e252c2a4e5744aa8b33ee9e29dd9d
#print(tecnico.auditar(),tecnico.getNombre(),tecnico.getLenguajes())