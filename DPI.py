dpi = input("ingresa tu DPI: ")
dep = ()

if  not dpi.isdigit():
    print("Error: El DPI solo debe contener números")
elif len(dpi) == 13:
    dep = dpi[9:11]
    muni = dpi[11:13]
    dep = int(dep)
    muni = int(muni)
else:
    print(f"Error: Se necesitan 13 dígitos. Ingresaste {len(dpi)}")


if dep == 1:
    print("Departamento de Guatemala")
    print("---------")
    print("Extencion territorial: 2.126 km")
    print("Idiomas hablados: Español, Kaqchiquel, Poqomam")
    print("Sitios turisticos: Ciudad de Guatemala")
    print("Rios: Las Vacas, Villa Lobos, Aguacapa")
    print("Lagos: Amatitlan")
    print("Poblacion: 3,573,179 habitantes")
    print("---------")
    # Diccionario de municipios Guatemala
    municipiosgt = {
    1: "Municipio de Guatemala",
    2: "Municipio de Santa Catarina Pinula",
    3: "Municipio de San Jose Pinula",
    4: "Municipio de San Jose Del Golfo",
    5: "Municipio de Palencia",
    6: "Municipio de Chinautla",
    7: "Municipio de San Pedro Ayampuc",
    8: "Municipio de Mixco",
    9: "Municipio de San Pedro Sacatepequez",
    10: "Municipio de San Juan Sacatepequez",
    11: "Municipio de San Raymundo",
    12: "Municipio de Chuarrancho",
    13: "Municipio de Fraijanes",
    14: "Municipio de Amatitlan",
    15: "Municipio de Villa Nueva",
    16: "Municipio de Villa Canales",
    17: "Municipio de San Miguel Petapa"}
    print(municipiosgt.get(muni, "Código de municipio no válido"))
if dep == 2:
    print("Departamento de El Progreso")
    print("---------")
    print("Extencion territorial: 1.922 km")
    print("Idiomas hablados: Español")
    print("Rios: Motagua o grande")
    print("Poblacion: 184,543 habitantes")
    print("---------")
    # Diccionario de municipios El Progreso
    municipiosprog = {
    1: "Municipio de Guastatoya",
    2: "Municipio de Morazán",
    3: "Municipio de San Agustín Acasaguastlán",
    4: "Municipio de San Cristóbal Acasaguastlán",
    5: "Municipio de El Jícaro",
    6: "Municipio de Sansare",
    7: "Municipio de Sanarate",
    8: "Municipio de San Antonio La Paz"
    }
    print(municipiosprog.get(muni, "Código de municipio no válido"))
if dep == 3:
    print("Departamento de Sacatepéquez")
    print("---------")
    print("Extensión territorial: 465 km²")
    print("Idiomas hablados: Español, Kaqchiquel")
    print("Sitios turísticos: Antigua Guatemala")
    print("Volcanes: Acatenango, de Agua, de Fuego")
    print("Ríos: Villa Lobos, Achiguate")
    print("Lagos: San Antonio Aguas Calientes")
    print("Población: 376,111 habitantes")
    print("---------")
    # Diccionario de municipios Sacatepéquez
    municipiossaca = {
    1: "Municipio de Antigua",
    2: "Municipio de Jocotenango",
    3: "Municipio de Pastores",
    4: "Municipio de Sumpango",
    5: "Municipio de Santo Domingo Xenacoj",
    6: "Municipio de Santiago Sacatepéquez",
    7: "Municipio de San Bartolomé Milpas Altas",
    8: "Municipio de San Lucas Sacatepéquez",
    9: "Municipio de Santa Lucía Milpas Altas",
    10: "Municipio de Magdalena Milpas Altas",
    11: "Municipio de Santa María de Jesús",
    12: "Municipio de Ciudad Vieja",
    13: "Municipio de San Miguel Dueñas",
    14: "Municipio de Alotenango",
    15: "Municipio de San Antonio Aguas Calientes",
    16: "Municipio de Santa Catarina Barahona"
    }
    print(municipiossaca.get(muni, "Código de municipio no válido"))
if dep == 4: 
    print("Departamento de Chimaltenango")
    print("---------")
    print("Extensión territorial: 1.979 km²")
    print("Idiomas hablados: Español, Kaqchiquel")
    print("Volcanes: Volcán de Fuego (límite)")
    print("Ríos: Río Madre Vieja, Pantaleón o Coyolate, Madre Vieja, Motagua, Xayá")
    print("Lagos: Lago de Chichoy")
    print("Población: 782,584 habitantes")
    print("---------")
    # Diccionario de municipios Chimaltenango
    municipioschi = {
    1: "Municipio de Chimaltenango",
    2: "Municipio de San José Poaquil",
    3: "Municipio de San Martín Jilotepeque",
    4: "Municipio de San Juan Comalapa",
    5: "Municipio de Santa Apolonia",
    6: "Municipio de Tecpán Guatemala",
    7: "Municipio de Patzún",
    8: "Municipio de San Miguel Pochuta",
    9: "Municipio de Patzicía",
    10: "Municipio de Santa Cruz Balanyá",
    11: "Municipio de Acatenango",
    12: "Municipio de San Pedro Yepocapa",
    13: "Municipio de San Andrés Itzapa",
    14: "Municipio de Parramos",
    15: "Municipio de Zaragoza",
    16: "Municipio de El Tejar"
    }
    print(municipioschi.get(muni, "Código de municipio no válido"))
    # Departamento de Escuintla (5)
if dep == 5:
    print("Departamento de Escuintla")
    print("---------")
    print("Extensión territorial: 4.384 km²")
    print("Idiomas hablados: Español, Kaqchiquel, Poqomam")
    print("Sitios turísticos: Volcán de Pacaya")
    print("Volcanes: Pacaya")
    print("Ríos: Villa Lobos, Pantaleón, Coyolate, Madre Vieja, Nahualate")
    print("Lagos: Amaya, De los Patos, QuitaSombrero, Chuaches, Chilín, El Corchal")
    print("Población: 832,311 habitantes")
    print("---------")
     # Diccionario de municipios Escuintla
    municipiosesc = {
    1: "Municipio de Escuintla",
    2: "Municipio de Santa Lucía Cotzumalguapa",
    3: "Municipio de La Democracia",
    4: "Municipio de Siquinalá",
    5: "Municipio de Masagua",
    6: "Municipio de Tiquisate",
    7: "Municipio de La Gomera",
    8: "Municipio de Guanagazapa",
    9: "Municipio de San José",
    10: "Municipio de Iztapa",
    11: "Municipio de Palín",
    12: "Municipio de San Vicente Pacaya",
    13: "Municipio de Nueva Concepción"
    }
    print(municipiosesc.get(muni, "Código de municipio no válido"))
# Departamento de Santa Rosa (6)
elif dep == 6:
    print("Departamento de Santa Rosa")
    print("---------")
    print("Extensión territorial: 2.995 km²")
    print("Idiomas hablados: Español")
    print("Volcanes: Tecuamburro, Jumaytepeque, Cruz Quemada, Cerro Redondo, Culma")
    print("Ríos: Los Esclavos, Santa Rosa, María Linda")
    print("Lagos: de Ayarza, de Ixpaco")
    print("Población: 415,108 habitantes")
    print("---------")
    # Diccionario de municipios Santa Rosa
    municipiosstar = {
    1: "Municipio de Cuilapa",
    2: "Municipio de Barberena",
    3: "Municipio de Santa Rosa de Lima",
    4: "Municipio de Casillas",
    5: "Municipio de San Rafael Las Flores",
    6: "Municipio de Oratorio",
    7: "Municipio de San Juan Tecuaco",
    8: "Municipio de Chiquimulilla",
    9: "Municipio de Taxisco",
    10: "Municipio de Santa María Ixhuatán",
    11: "Municipio de Guazacapán",
    12: "Municipio de Santa Cruz Naranjo",
    13: "Municipio de Pueblo Nuevo Viñas",
    14: "Municipio de Nueva Santa Rosa"
    }
    print(municipiosstar.get(muni, "Código de municipio no válido"))

# Departamento de Sololá (7)
elif dep == 7:
    print("Departamento de Sololá")
    print("---------")
    print("Extensión territorial: 1.061 km²")
    print("Idiomas hablados: Español, Kaqchiquel, K'iche', Tz'utujil")
    print("Sitios turísticos: Lago de Atitlán")
    print("Volcanes: Atitlán, Tolimán, San Pedro")
    print("Ríos: Nahualate, Madre Vieja, Tzalá")
    print("Lagos: Lago de Atitlán")
    print("Población: 562,792 habitantes")
    print("---------")
    # Diccionario de municipios Solola
    municipiossl = {
    1: "Municipio de Sololá",
    2: "Municipio de San José Chacayá",
    3: "Municipio de Santa María Visitación",
    4: "Municipio de Santa Lucía Utatlán",
    5: "Municipio de Nahualá",
    6: "Municipio de Santa Catarina Ixtahuacán",
    7: "Municipio de Santa Clara La Laguna",
    8: "Municipio de Concepción",
    9: "Municipio de San Andrés Semetabaj",
    10: "Municipio de Panajachel",
    11: "Municipio de Santa Catarina Palopó",
    12: "Municipio de San Antonio Palopó",
    13: "Municipio de San Lucas Tolimán",
    14: "Municipio de Santa Cruz La Laguna",
    15: "Municipio de San Pablo La Laguna",
    16: "Municipio de San Marcos La Laguna",
    17: "Municipio de San Juan La Laguna",
    18: "Municipio de San Pedro La Laguna",
    19: "Municipio de Santiago Atitlán"
    }
    print(municipiossl.get(muni, "Código de municipio no válido"))

# Departamento de Totonicapán (8)
elif dep == 8:
    print("Departamento de Totonicapán")
    print("---------")
    print("Extensión territorial: 1.061 km²")
    print("Idiomas hablados: Español, K'iche'")
    print("Volcanes: Cuxliquel")
    print("Ríos: Xequijel, Negro, Nahualate")
    print("Lagos: Laguna Chicabal")
    print("Población: 618,077 habitantes")
    print("---------")
    # Diccionario de municipios Totonicapán
    municipiostot = {
    1: "Municipio de Totonicapán",
    2: "Municipio de San Cristóbal Totonicapán",
    3: "Municipio de San Francisco El Alto",
    4: "Municipio de San Andrés Xecul",
    5: "Municipio de Momostenango",
    6: "Municipio de Santa María Chiquimula",
    7: "Municipio de Santa Lucía La Reforma",
    8: "Municipio de San Bartolo Aguas Calientes"
    }
    print(municipiostot.get(muni, "Código de municipio no válido"))

# Departamento de Quetzaltenango (9)
elif dep == 9:
    print("Departamento de Quetzaltenango")
    print("---------")
    print("Extensión territorial: 1.953 km²")
    print("Idiomas hablados: Español, Mam, K'iche'")
    print("Sitios turísticos: Fuentes Georginas")
    print("Volcanes: Santa María, Zunil, Orejas, Cerro Quemado, Chicabal, Santiaguito")
    print("Ríos: Ocosito, Xequijel, Cuilco, Naranjo")
    print("Lagos: Laguna de Chicabal, Cuaches")
    print("Población: 959,047 habitantes")
    print("---------")
    # Diccionario de municipios Quetzaltenango
    municipiosqtz = {
    1: "Municipio de Quetzaltenango",
    2: "Municipio de Salcajá",
    3: "Municipio de Olintepeque",
    4: "Municipio de San Carlos Sija",
    5: "Municipio de Sibilia",
    6: "Municipio de Cabricán",
    7: "Municipio de Cajolá",
    8: "Municipio de San Miguel Sigüilá",
    9: "Municipio de San Juan Ostuncalco",
    10: "Municipio de San Mateo",
    11: "Municipio de Concepción Chiquirichapa",
    12: "Municipio de San Martín Sacatepéquez",
    13: "Municipio de Almolonga",
    14: "Municipio de Cantel",
    15: "Municipio de Huitán",
    16: "Municipio de Zunil",
    17: "Municipio de Colomba Costa Cuca",
    18: "Municipio de San Francisco La Unión",
    19: "Municipio de El Palmar",
    20: "Municipio de Coatepeque",
    21: "Municipio de Génova Costa Cuca",
    22: "Municipio de Flores Costa Cuca",
    23: "Municipio de La Esperanza",
    24: "Municipio de Palestina De Los Altos"
    }
    print(municipiosqtz.get(muni, "Código de municipio no válido"))

# Departamento de Suchitepéquez (10)
elif dep == 10:
    print("Departamento de Suchitepéquez")
    print("---------")
    print("Extensión territorial: 2.510 km²")
    print("Idiomas hablados: Español, K'iche', Kaqchiquel, Tz'utujil")
    print("Ríos: Sis, Nahualate, Madre Vieja, Samalá")
    print("Lagos: Chiquistepeque")
    print("Población: 638,137 habitantes")
    print("---------")
    # Diccionario de municipios Suchitepéquez
    municipiossuch = {
    1: "Municipio de Mazatenango",
    2: "Municipio de Cuyotenango",
    3: "Municipio de San Francisco Zapotitlán",
    4: "Municipio de San Bernardino",
    5: "Municipio de San José El Ídolo",
    6: "Municipio de Santo Domingo Suchitepéquez",
    7: "Municipio de San Lorenzo",
    8: "Municipio de Samayac",
    9: "Municipio de San Pablo Jocopilas",
    10: "Municipio de San Antonio Suchitepéquez",
    11: "Municipio de San Miguel Panán",
    12: "Municipio de San Gabriel",
    13: "Municipio de Chicacao",
    14: "Municipio de Patulul",
    15: "Municipio de Santa Bárbara",
    16: "Municipio de San Juan Bautista",
    17: "Municipio de Santo Tomás La Unión",
    18: "Municipio de Zunilito",
    19: "Municipio de Pueblo Nuevo",
    20: "Municipio de Río Bravo"
    }
    print(municipiossuch.get(muni, "Código de municipio no válido"))
# Departamento de Retalhuleu (11)
if dep == 11:
    print("Departamento de Retalhuleu")
    print("---------")
    print("Extensión territorial: 1.856 km²")
    print("Idiomas hablados: Español, K'iche'")
    print("Ríos: Samalá, Ocosito, Sis")
    print("Lagos: Aguacatán, Balonas, Corchal, Chachitas, Espinola, Escondida, Grande")
    print("Población: 369,863 habitantes")
    print("---------")
    # Diccionario de municipios Retalhuleu
    municipiosret = {
    1: "Municipio de Retalhuleu",
    2: "Municipio de San Sebastián",
    3: "Municipio de Santa Cruz Muluá",
    4: "Municipio de San Martín Zapotitlán",
    5: "Municipio de San Felipe",
    6: "Municipio de San Andrés Villa Seca",
    7: "Municipio de Champerico",
    8: "Municipio de Nuevo San Carlos",
    9: "Municipio de El Asintal"
    }
    print(municipiosret.get(muni, "Código de municipio no válido"))

# Departamento de San Marcos (12)
elif dep == 12:
    print("Departamento de San Marcos")
    print("---------")
    print("Extensión territorial: 3.791 km²")
    print("Idiomas hablados: Español, Mam, Kaqchiquel, Sipakapense")
    print("Volcanes: Tajumulco, Tacaná")
    print("Ríos: Suchiate, Naranjo, Cuilco")
    print("Población: 1,250,306 habitantes")
    print("---------")
    # Diccionario de municipios San Marcos
    municipiossm = {
    1: "Municipio de San Marcos",
    2: "Municipio de San Pedro Sacatepéquez",
    3: "Municipio de San Antonio Sacatepéquez",
    4: "Municipio de Comitancillo",
    5: "Municipio de San Miguel Ixtahuacán",
    6: "Municipio de Concepción Tutuapa",
    7: "Municipio de Tacaná",
    8: "Municipio de Sibinal",
    9: "Municipio de Tajumulco",
    10: "Municipio de Tejutla",
    11: "Municipio de San Rafael Pie de la Cuesta",
    12: "Municipio de Nuevo Progreso",
    13: "Municipio de El Tumbador",
    14: "Municipio de San José El Rodeo",
    15: "Municipio de Malacatán",
    16: "Municipio de Catarina",
    17: "Municipio de Ayutla",
    18: "Municipio de Ocos",
    19: "Municipio de San Pablo",
    20: "Municipio de El Quetzal",
    21: "Municipio de La Reforma",
    22: "Municipio de Pajapita",
    23: "Municipio de Ixchiguán",
    24: "Municipio de San José Ojetenam",
    25: "Municipio de San Cristóbal Cucho",
    26: "Municipio de Sipacapa",
    27: "Municipio de Esquipulas Palo Gordo",
    28: "Municipio de Río Blanco",
    29: "Municipio de San Lorenzo"
    }
    print(municipiossm.get(muni, "Código de municipio no válido"))

# Departamento de Huehuetenango (13)
elif dep == 13:
    print("Departamento de Huehuetenango")
    print("---------")
    print("Extensión territorial: 7.400 km²")
    print("Idiomas hablados: Español, Mam, Ch'orti', Akateko, Awakateko, Popti', Q'anjob'al, Tektiteko")
    print("Ríos: Ixcán, Nentón, Seleguá, Cuilco")
    print("Lagos: Yolnajab, Maxbal")
    print("Población: 1,409,756 habitantes")
    print("---------")
    # Diccionario de municipios Huehuetenango
    municipioshue = {
    1: "Municipio de Huehuetenango",
    2: "Municipio de Chiantla",
    3: "Municipio de Malacatancito",
    4: "Municipio de Cuilco",
    5: "Municipio de Nentón",
    6: "Municipio de San Pedro Necta",
    7: "Municipio de Jacaltenango",
    8: "Municipio de San Pedro Soloma",
    9: "Municipio de San Ildefonso Ixtahuacán",
    10: "Municipio de Santa Bárbara",
    11: "Municipio de La Libertad",
    12: "Municipio de La Democracia",
    13: "Municipio de San Miguel Acatán",
    14: "Municipio de San Rafael La Independencia",
    15: "Municipio de Todos Santos Cuchumatán",
    16: "Municipio de San Juan Atitán",
    17: "Municipio de Santa Eulalia",
    18: "Municipio de San Mateo Ixtatán",
    19: "Municipio de Colotenango",
    20: "Municipio de San Sebastián Huehuetenango",
    21: "Municipio de Tectitán",
    22: "Municipio de Concepción Huista",
    23: "Municipio de San Juan Ixcoy",
    24: "Municipio de San Antonio Huista",
    25: "Municipio de San Sebastián Coatán",
    26: "Municipio de Santa Cruz Barillas",
    27: "Municipio de Aguacatán",
    28: "Municipio de San Rafael Petzal",
    29: "Municipio de San Gaspar Ixchil",
    30: "Municipio de Santiago Chimaltenango",
    31: "Municipio de Santa Ana Huista",
    32: "Municipio de Unión Cantinil"
    }
    print(municipioshue.get(muni, "Código de municipio no válido"))
# Departamento Quiché 14
if dep == 14:
	print("Departamento de Quiché")
	print("---------")
	print("Extensión territorial: 8.378 km²")
	print("Idiomas hablados: Español, Ixil, Kiche, Qeqchi, Sakapulteko, Uspanteko")
	print("Ríos: Xalbal, Sichel, Negro, Motagua")
	print("Lagos: Laguna Lemoa")
	print("Población: 1,276,936 habitantes")
	print("---------")
     # Diccionario de municipios Quiché
	municipiosche = {
    1: "Santa Cruz del Quiché",
    2: "Chiche",
    3: "Chinique",
    4: "Zacualpa",
    5: "Chajul",
    6: "Sto Tomas Chichicastenango",
    7: "Patzité",
    8: "San Antonio Ilotenango",
    9: "San Pedro Jocopilas",
    10: "Cunén",
    11: "San Juan Cotzal",
    12: "Joyabaj",
    13: "Nebaj",
    14: "San Andrés Sajcabajá",
    15: "San Miguel Uspantán",
    16: "Sacapulas",
    17: "San Bartolomé Jocotenango",
    18: "Canillá",
    19: "Chicamán",
    20: "Ixcán",
    21: "Pachalum",
    22: "Playa Grande"
	}
	print(municipiosche.get(muni, "Código de municipio no válido"))

# Departamento Baja Verapaz 15
if dep == 15:
	print("Departamento de Baja Verapaz")
	print("---------")
	print("Extensión territorial: 3.124 km²")
	print("Idiomas hablados: Español, Poqomchi, Kaqchiquel, Achi, Xinca")
	print("Ríos: Río Negro")
	print("Lagos: Lago de Embalse Chixoy")
	print("Población: 339,873 habitantes")
	print("---------")
     # Diccionario de municipios Baja Verapaz
	municipiosbaj = {
    1: "Salamá",
    2: "San Miguel Chicaj",
    3: "Rabinal",
    4: "Cubulco",
    5: "Granados",
    6: "Santa Cruz El Chol",
    7: "San Jerónimo",
    8: "Purulhá"
	}
	print(municipiosbaj.get(muni, "Código de municipio no válido"))

# Departamento Alta Verapaz 16
if dep == 16:
	print("Departamento de Alta Verapaz")
	print("---------")
	print("Extensión territorial: 8.686 km²")
	print("Idiomas hablados: Español, Poqomchi, Qeqchi")
	print("Sitios turísticos: Laguna Lachuá, Semuc Champey")
	print("Ríos: Modesto Méndez, Polochic, Cahabón, Negro")
	print("Lagos: Laguna Lachuá")
	print("Población: 1,450,280 habitantes")
	print("---------")
	municipiosalv = {
    1: "Cobán",
    2: "Santa Cruz Verapaz",
    3: "San Cristóbal Verapaz",
    4: "Tactic",
    5: "Tamahú",
    6: "San Miguel Tucurú",
    7: "Panzós",
    8: "Senahú",
    9: "San Pedro Carchá",
    10: "San Juan Chamelco",
    11: "Lanquín",
    12: "Santa María Cahabón",
    13: "Chisec",
    14: "Chahal",
    15: "Fray Bartolomé de las Casas",
    16: "La Tinta",
    17: "Raxruhá"
	}
	print(municipiosalv.get(muni, "Código de municipio no válido"))
# Departamento Petén 17
if dep == 17:
    print("Departamento de Petén")
    print("---------")
    print("Extensión territorial: 35,854 km²")
    print("Idiomas hablados: Español, ItzaMopán, Qeqchi")
    print("Sitios turísticos: El Remate, Isla de Flores, Tikal, Cráter Azul")
    print("Ríos: Candelaria, Tikal, Usumacinta, Salinas, La Pasión, San Juan, Santa Isabel, Modesto Mendez")
    print("Lagos: Petén Itzá, El Tigre, Yaxhá, Perdida, San Diego, Mendoza")
    print("Población: 858,256 habitantes")
    print("---------")
    
    # Diccionario de municipios Petén
    municipiospeten = {
    1: "Flores",
    2: "San José",
    3: "San Benito",
    4: "San Andrés",
    5: "La Libertad",
    6: "San Francisco",
    7: "Santa Ana",
    8: "Dolores",
    9: "San Luis",
    10: "Sayaxché",
    11: "Melchor De Mencos",
    12: "Poptún"
    }
    print(municipiospeten.get(muni, "Código de municipio no válido"))

# Departamento Izabal 18
if dep == 18:
    print("Departamento de Izabal")
    print("---------")
    print("Extensión territorial: 9,038 km²")
    print("Idiomas hablados: Español, Garifuna, Qeqchi")
    print("Sitios turísticos: Río Dulce, Castillo de San Felipe, Playa Blanca")
    print("Ríos: Chocón Machaca, Dulce, Motagua, Polochic, Sarstén")
    print("Lagos: Lago de Izabal")
    print("Población: 512,242 habitantes")
    print("---------")
    
    # Diccionario de municipios Izabal
    municipiosizabal = {
    1: "Puerto Barrios",
    2: "Livingston",
    3: "El Estor",
    4: "Morales",
    5: "Los Amates"
    }
    print(municipiosizabal.get(muni, "Código de municipio no válido"))

# Departamento Zacapa 19
if dep == 19:
    print("Departamento de Zacapa")
    print("---------")
    print("Extensión territorial: 2,690 km²")
    print("Idiomas hablados: Español, Chorti")
    print("Ríos: Río Teculután, Grande de Zacapa, El Tambor, Motagua")
    print("Población: 257,832 habitantes")
    print("---------")
    
    # Diccionario de municipios Zacapa
    municipioszacapa = {
    1: "Zacapa",
    2: "Estanzuela",
    3: "Río Hondo",
    4: "Gualán",
    5: "Teculután",
    6: "Usumatlán",
    7: "Cabañas",
    8: "San Diego",
    9: "La Unión",
    10: "Huité"
    }
    print(municipioszacapa.get(muni, "Código de municipio no válido"))

# Departamento Chiquimula 20
if dep == 20:
    print("Departamento de Chiquimula")
    print("---------")
    print("Extensión territorial: 2,376 km²")
    print("Idiomas hablados: Español, Chorti")
    print("Volcanes: Quetzaltepeque, Ipala límite")
    print("Ríos: Jocotán, Shutaque, San José")
    print("Lagos: Laguna del Jute")
    print("Población: 455,645 habitantes")
    print("---------")
    
    # Diccionario de municipios Chiquimula
    municipioschiquimula = {
    1: "Chiquimula",
    2: "San José La Arada",
    3: "San Juan La Ermita",
    4: "Jocotán",
    5: "Camotán",
    6: "Olopa",
    7: "Esquipulas",
    8: "Concepción Las Minas",
    9: "Quezaltepeque",
    10: "San Jacinto",
    11: "Ipala"
    }
    print(municipioschiquimula.get(muni, "Código de municipio no válido"))

# Departamento Jalapa 21
if dep == 21:
    print("Departamento de Jalapa")
    print("---------")
    print("Extensión territorial: 2,063 km²")
    print("Idiomas hablados: Español, Poqomam")
    print("Volcanes: Jumay, Tobón, Alzatate, Tahual, Monterico")
    print("Ríos: Paz, Cusmapa, Ostúa")
    print("Lagos: Laguna Los Achiotes, de Hoyo")
    print("Población: 407,125 habitantes")
    print("---------")
    
    # Diccionario de municipios Jalapa
    municipiosjalapa = {
    1: "Jalapa",
    2: "San Pedro Pinula",
    3: "San Luis Jilotepeque",
    4: "San Manuel Chaparrón",
    5: "San Carlos Alzatate",
    6: "Monjas",
    7: "Mataquescuintla"
    }
    print(municipiosjalapa.get(muni, "Código de municipio no válido"))

# Departamento Jutiapa 22
if dep == 22:
    print("Departamento de Jutiapa")
    print("---------")
    print("Extensión territorial: 3,216 km²")
    print("Idiomas hablados: Español")
    print("Sitios turísticos: Laguna y Volcán de Ipala")
    print("Volcanes: Suchitán, Jutiapa, Moyuta, Ipala límite, Ixtepeque, Culma, Las Víbora, Amayo")
    print("Lagos: Lago de Gúija")
    print("Población: 525,022 habitantes")
    print("---------")
    
    # Diccionario de municipios Jutiapa
    municipiosjutiapa = {
    1: "Jutiapa",
    2: "El Progreso",
    3: "Santa Catarina Mita",
    4: "Agua Blanca",
    5: "Asunción Mita",
    6: "Yupiltepeque",
    7: "Atescatempa",
    8: "Jerez",
    9: "El Adelanto",
    10: "Zapotitlán",
    11: "Comapa",
    12: "Jalpatagua",
    13: "Conguaco",
    14: "Moyuta",
    15: "Pasaco",
    16: "San José Acatempa",
    17: "Quesada"
    }
    print(municipiosjutiapa.get(muni, "Código de municipio no válido"))
