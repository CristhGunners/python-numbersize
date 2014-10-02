python-numbersize
=================

## Como usar

Solo necesitamos bajar el archivo e incluirlo en nuestro proyecto.
Una vez listo este paso, procedemos a llamar a numbersize
    
      from numbersize import abbr,normal,decimal
      
      # abbr es la funcion que realizara la conversión
      # normal y decimal son los sistemas de conversión
      
      bignumber = 3000
      abbnumber = abbr(bignumber,normal)
      print(abbnumber)
      >> 3K
      
      bigdecimal = 1024
      abbdecimal = abbr(bigdecimal,decimal)
      print(abbdecimal)
      >> 1K
      

## Sistema de conversión

El sistema normal contempla las siguientes opciones:

- KB
- MB
- GB
- TB
- PB

El sistema decimal comtempla las siguientes opciones:

- K
- M
- G
- T
- P

