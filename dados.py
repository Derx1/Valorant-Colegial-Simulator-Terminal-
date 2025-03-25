NOMES_JOGADORES = [
    "João", "Pedro", "Lucas", "Gabriel", "Matheus", "Felipe", "Gustavo", 
    "Rafael", "Diego", "Thiago", "Bruno", "Eduardo", "Vinícius", "André", 
    "Rodrigo", "Daniel", "Leonardo", "Caio", "Henrique", "Ricardo", "Miguel", 
    "Vitor", "Fernando", "Marcelo", "Alexandre", "Carlos", "Igor", "Guilherme",
    "Samuel", "Paulo", "Juliano", "Renan", "Evandro", "Rogério", "Cauã", 
    "Arthur", "Davi", "Enzo", "Bernardo", "Murilo", "Emanuel", "Otávio", 
    "Antônio", "Luiz", "Raul", "Breno", "Kauê", "Francisco", "Ruan", "Luan",
    "Leandro", "Marcos", "Cristiano", "Jorge", "Roberto", "Sérgio", "Hugo",
    "Márcio", "Cláudio", "José"
]
SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves",
    "Pereira", "Lima", "Costa", "Gomes", "Martins", "Rocha", "Ribeiro", "Carvalho",
    "Melo", "Cardoso", "Teixeira", "Nascimento", "Barbosa", "Cunha", "Neves",
    "Monteiro", "Moreira", "Correia", "Borges", "Guimarães", "Mendes", "Dias",
    "Castro", "Campos", "Freitas", "Araújo", "Nogueira", "Machado", "Andrade",
    "Sousa", "Pinto", "Moraes", "Azevedo", "Vieira", "Barros", "Reis", "Lopes",
    "Xavier", "Tavares", "Peixoto", "Farias", "Aguiar", "Vasconcelos", "Marques",
    "Medeiros", "Britto", "Quintana", "Duarte", "Valente", "Cavalcanti"
]

NOMES_TIMES = [
    "Colégio São Paulo", "Instituto Educacional Brasil", "Escola Técnica Rio de Janeiro",
    "Colégio Minas Gerais", "Escola Bahia de Ensino", "Instituto Paraná", 
    "Colégio Santa Catarina", "Escola Pernambuco", "Ginásio Goiás", 
    "Colégio Ceará Educacional", "Escola Amazonas", "Instituto Espírito Santo",
    "Colégio Sergipe", "Escola Paraíba", "Ginásio Piauí", "Colégio Alagoas",
    "Escola Mato Grosso", "Instituto Rondônia", "Colégio Acre", 
    "Escola Tocantins Futuro", "Academia Maranhão", "Centro Educacional Rio Grande do Sul",
    "Colégio Mato Grosso do Sul", "Instituto Amapá", "Escola Técnica Pará", 
    "Ginásio Roraima", "Colégio Rio Grande do Norte", "Instituto Maranhão de Ciências",
    "Escola Piauí Tecnológico", "Colégio Distrito Federal", "Academia Rondônia", 
    "Instituto Sergipe de Esportes"
]
TODOS_MAPAS = [
    "Abyss", "Fracture", "Bind", "Haven", "Pearl", 
    "Split", "Lotus", "Ascent", "Breeze", "Icebox", 
    "Sunset"
]

MAPAS_INICIAIS = ["Abyss", "Fracture", "Bind", "Haven", "Pearl", "Split", "Lotus"]
AGENTES_POR_FUNCAO = {
    "Duelista": ["Jett", "Phoenix", "Reyna", "Raze", "Yoru","Iso","Neon","Waylay"],
    "Controlador": ["Omen", "Brimstone", "Viper", "Astra", "Harbor","Clove"],
    "Sentinela": ["Sage", "Killjoy", "Cypher", "Chamber","Vyse","Deadlock"],
    "Iniciador": ["Sova", "Breach", "Skye", "KAY/O", "Fade", "Gekko","Tejo"],
    "Flex": ["Jett", "Phoenix", "Reyna", "Raze", "Yoru","Iso","Neon","Omen", "Brimstone", "Viper", "Astra", "Harbor","Clove","Sage", "Killjoy", "Cypher", "Chamber","Vyse","Deadlock","Sova", "Breach", "Skye", "KAY/O", "Fade", "Gekko", "Tejo"]  # Pode usar qualquer agente
}

NOMES_JOGADORES_INTERNACIONAIS = {
    "Japão": [
        "Haruto", "Yuki", "Riku", "Souta", "Ren", "Itsuki", "Kaoru", "Akira", "Hiroto", "Kaito",
        "Hinata", "Sora", "Reo", "Daiki", "Ryota", "Aoi", "Tsubasa", "Nao", "Kazuki", "Shota",
        "Minato", "Taiga", "Kota", "Yuji", "Asahi", "Masaki", "Keisuke", "Takumi", "Kazuya", "Takahiro",
        "Yuta", "Tomoya", "Shoichi", "Kenji", "Tetsuya", "Ryusei", "Shinji", "Makoto", "Ryohei", "Kenta",
        "Sho", "Kosuke", "Renji", "Hikaru", "Seiji", "Hiroshi", "Kazuma", "Eiji", "Ryuki", "Takuto"],
  "Coreia do Sul": [
        "Min-ho", "Jin-woo", "Sung-min", "Jae-hyun", "Tae-yong", "Hyun-jin", "Ji-hoon", "Seung-ho", "Dong-hyun", "Yong-jin",
        "Soo-jin", "Eun-ji", "Hye-jin", "Yoon-seo", "Seo-yeon", "Ji-yoon", "Ha-eun", "Min-seo", "Ye-jin", "Sun-woo",
        "Jung-ho", "Chul-soo", "Kyung-ho", "Dae-hyun", "Hwan", "Geon-woo", "Woo-jin", "Yeon-jun", "Do-hyun", "Byung-ho",
        "Chang-min", "In-soo", "Myung-ho", "Seok-jin", "Joon-ho", "Hyeon-woo", "Jin-seok", "Sang-ho", "Kwan-woo", "Jae-won",
        "Kyung-min", "Min-woo", "Jin-young", "Seung-min", "Hyo-jin", "Woo-seok", "Young-soo", "Jung-woo", "Jong-ho", "Dong-jin"
    ],
    "China": [
        "Wei", "Li", "Zhang", "Ming", "Feng", "Chen", "Yang", "Cheng", "Jian", "Xiang",
        "Hua", "Bo", "Jun", "Tian", "Guang", "Long", "Yuan", "Lei", "Hao", "Ping",
        "Yu", "Hui", "Xiao", "Shan", "Qiang", "Ying", "Lin", "Yong", "Hong", "Kun",
        "Ren", "Sheng", "Jie", "Hai", "Qing", "Fei", "Bin", "Zhi", "Biao", "Dong",
        "Xun", "Gang", "Rui", "Jin", "Xue", "Cai", "Kai", "Tao", "Nan", "Shuo"
    ],
    "Estados Unidos": [
        "Michael", "James", "William", "John", "Robert", "David", "Joseph", "Thomas", "Christopher", "Daniel",
        "Matthew", "Anthony", "Mark", "Donald", "Paul", "Steven", "Andrew", "Joshua", "Kevin", "Brian",
        "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Nicholas", "Gary",
        "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Frank",
        "Gregory", "Raymond", "Alexander", "Patrick", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Henry"
    ],
    "Brasil": [
        "João", "Pedro", "Lucas", "Gabriel", "Matheus", "Rafael", "Felipe", "Gustavo", "Diego", "Thiago",
        "Bruno", "Eduardo", "Vinícius", "André", "Rodrigo", "Daniel", "Leonardo", "Caio", "Henrique", "Ricardo",
        "Miguel", "Jorge", "Antonio", "Luiz", "Victor", "Fernando", "Marcelo", "Alexandre", "Márcio", "Fábio",
        "Murilo", "Samuel", "Vitor", "Paulo", "Juliano", "Renan", "Evandro", "Rogério", "Igor", "Guilherme",
        "César", "Adriano", "Renato", "Hugo", "Otávio", "Ronaldo", "Christian", "Tiago", "Cauã", "Arthur"
    ],
    "Alemanha": [
        "Hans", "Peter", "Jürgen", "Klaus", "Wolfgang", "Uwe", "Heinz", "Frank", "Stefan", "Karl",
        "Friedrich", "Georg", "Werner", "Johann", "Otto", "Thomas", "Horst", "Rolf", "Dirk", "Andreas",
        "Günther", "Heinrich", "Paul", "Arno", "Michael", "Alexander", "Martin", "Bernhard", "Dietrich", "Erich",
        "Fritz", "Manfred", "Joachim", "Wilhelm", "Lothar", "Christoph", "Matthias", "Bernd", "Axel", "Jan",
        "Siegfried", "Konrad", "Norbert", "Rainer", "Helmut", "Ulrich", "Herbert", "Reinhard", "Ewald", "Eberhard"
    ],
    "França": [
        "Jean", "Pierre", "Jacques", "Michel", "Luc", "Louis", "Antoine", "Henri", "Julien", "Charles",
        "François", "Philippe", "Thomas", "André", "Claude", "Victor", "Paul", "Gérard", "Robert", "Georges",
        "Marc", "Bernard", "Nicolas", "Laurent", "Yves", "Olivier", "Pascal", "Thierry", "Christophe", "Damien",
        "Hugo", "Arnaud", "Vincent", "Sébastien", "Cédric", "Maxime", "Éric", "Alexandre", "Jules", "Fabrice",
        "Bruno", "Félix", "Benjamin", "Tristan", "René", "Étienne", "Lionel", "Daniel", "Dominique", "Gilbert"
    ],
    "Itália": [
        "Giovanni", "Luca", "Marco", "Francesco", "Alessandro", "Antonio", "Paolo", "Matteo", "Stefano", "Fabio",
        "Leonardo", "Davide", "Giuseppe", "Roberto", "Giorgio", "Alberto", "Simone", "Enrico", "Claudio", "Salvatore",
        "Daniele", "Carlo", "Nicola", "Michele", "Luigi", "Federico", "Riccardo", "Emanuele", "Pietro", "Gabriele",
        "Vincenzo", "Angelo", "Alessio", "Andrea", "Massimo", "Cristiano", "Maurizio", "Alessandro", "Raffaele", "Valerio",
        "Sergio", "Fabiano", "Ruggero", "Tommaso", "Rinaldo", "Ettore", "Mario", "Cesare", "Marcello", "Flavio"
    ],
    "Espanha": [
        "Carlos", "Juan", "Luis", "Manuel", "Francisco", "Javier", "Antonio", "Miguel", "José", "Diego",
        "Ángel", "Rafael", "Sergio", "Alejandro", "Daniel", "Fernando", "Ricardo", "Rubén", "Pablo", "Alberto",
        "Jorge", "Adrián", "Mario", "Víctor", "Julián", "Pedro", "Álvaro", "Roberto", "Raúl", "Eduardo",
        "Tomás", "Gabriel", "Héctor", "Ignacio", "Enrique", "Félix", "Cristian", "Ramón", "Ismael", "Saúl",
        "Nicolás", "Andrés", "Esteban", "Samuel", "Domingo", "Santiago", "Hugo", "Mateo", "Iker", "Óscar"
    ],
    "Argentina": [
        "Santiago", "Mateo", "Nicolás", "Joaquín", "Lucas", "Martín", "Juan", "Tomás", "Matías", "Diego",
        "Franco", "Emiliano", "Julian", "Agustín", "Ignacio", "Gabriel", "Facundo", "Ramiro", "Bruno", "Sebastián",
        "Alejandro", "Francisco", "Hernán", "Lautaro", "Gonzalo", "Leandro", "Rodrigo", "Mariano", "Federico", "Mauricio",
        "Rafael", "Cristian", "Esteban", "Valentín", "Luciano", "Andrés", "Nahuel", "Manuel", "Álvaro", "Pablo",
        "Ezequiel", "Gerardo", "Fernando", "Javier", "Carlos", "Hugo", "Maximiliano", "Ricardo", "Patricio", "Damián"
    ],
    "México": [
        "José", "Luis", "Juan", "Carlos", "Miguel", "Francisco", "Jorge", "Ricardo", "Pedro", "Raúl",
        "Manuel", "Antonio", "Alejandro", "Fernando", "Javier", "Eduardo", "Rafael", "Daniel", "Cristian", "Diego",
        "Adrián", "Ángel", "Rubén", "Gabriel", "Andrés", "Marco", "Emilio", "Óscar", "Hugo", "Ramiro",
        "Jesús", "Guillermo", "Roberto", "Vicente", "Iván", "Héctor", "Salvador", "Esteban", "Mario", "Álvaro",
        "Gonzalo", "Tomás", "Félix", "Mauricio", "Mateo", "Luciano", "Arturo", "Ismael", "Rodrigo", "Felipe"
    ],
    "Inglaterra": [
        "Oliver", "George", "Harry", "Jack", "Jacob", "Charlie", "Thomas", "William", "Henry", "James",
        "Oscar", "Archie", "Alfie", "Freddie", "Theodore", "Leo", "Alexander", "Edward", "Arthur", "Benjamin",
        "Samuel", "Ethan", "Sebastian", "Joseph", "Lucas", "Daniel", "Joshua", "Matthew", "Ryan", "Adam",
        "Toby", "Nathan", "David", "Finn", "Reuben", "Callum", "Harrison", "Liam", "Louis", "Isaac",
        "Zachary", "Jamie", "Elliot", "Jayden", "Mason", "Charles", "Caleb", "Aaron", "Harvey", "Riley"
    ],
    "Rússia": [
        "Ivan", "Dmitry", "Alexei", "Nikolai", "Sergei", "Andrei", "Vladimir", "Yuri", "Maxim", "Mikhail",
        "Boris", "Oleg", "Kirill", "Pavel", "Arkady", "Artem", "Roman", "Fyodor", "Viktor", "Konstantin",
        "Alexandr", "Timofei", "Vadim", "Vasily", "Egor", "Daniil", "Igor", "Stanislav", "Grigory", "Gennady",
        "Stepan", "Leonid", "Anatoly", "Lev", "Nikita", "Sergey", "Ruslan", "Evgeny", "Zinoviy", "Gavriil",
        "Yegor", "Matvey", "Andrey", "Arseniy", "Ilya", "Oleg", "Vyacheslav", "Semyon", "Gleb", "Platon"
    ],
    "Canadá": [
        "Liam", "Noah", "Oliver", "Lucas", "Ethan", "Benjamin", "William", "Jacob", "James", "Alexander",
        "Logan", "Mason", "Jack", "Henry", "Owen", "Aiden", "Leo", "Sebastian", "Daniel", "Matthew",
        "Nathan", "Joseph", "Elijah", "Samuel", "David", "Christopher", "Jackson", "Connor", "Caleb", "Carter",
        "Ryan", "Isaac", "Gabriel", "Luke", "Hudson", "Dylan", "Aaron", "Hunter", "Wyatt", "Nicholas",
        "Adam", "Michael", "Andrew", "Nathaniel", "Elliot", "Landon", "Dominic", "Zachary", "Grayson", "Colton"
    ],
    "Austrália": [
        "Liam", "Noah", "Oliver", "Jack", "William", "James", "Lucas", "Thomas", "Ethan", "Alexander",
        "Charlie", "Henry", "Levi", "Oscar", "Elijah", "Leo", "Sebastian", "Harrison", "Benjamin", "Archer",
        "Joshua", "Samuel", "Hunter", "Hudson", "Logan", "Archie", "Eli", "Daniel", "Mason", "Nathan",
        "Flynn", "Cooper", "Ryder", "Blake", "Lachlan", "Ryan", "Austin", "Jaxon", "Xavier", "Miles",
        "Aaron", "Zachary", "Maxwell", "Elliott", "Joseph", "Gabriel", "Kai", "Aiden", "Callum", "Beau"
    ],
    "Portugal": [
        "João", "Pedro", "Gonçalo", "Miguel", "Rui", "Tiago", "Ricardo", "André", "Diogo", "Nuno",
        "Francisco", "Manuel", "António", "Carlos", "Eduardo", "Filipe", "José", "Paulo", "Hugo", "Artur",
        "Vasco", "Luís", "Rafael", "Daniel", "Alexandre", "Tomás", "Rodrigo", "Jorge", "Mário", "Frederico",
        "Cristiano", "Salvador", "Henrique", "Bruno", "Mateus", "Leandro", "Simão", "Sérgio", "David", "Domingos",
        "Adriano", "Martim", "Rui", "Duarte", "Gabriel", "Lucas", "Leonardo", "Caetano", "Vicente", "Telmo"
    ],
    "Índia": [
        "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Krishna", "Ishaan", "Shiv",
        "Rohan", "Aryan", "Dhruv", "Ansh", "Kabir", "Karthik", "Parth", "Rudra", "Om", "Ayaan",
        "Laksh", "Dev", "Jai", "Siddharth", "Harsh", "Yash", "Rahul", "Aman", "Manav", "Varun",
        "Rishi", "Tushar", "Gaurav", "Madhav", "Shaurya", "Raghav", "Kunal", "Tejas", "Nikhil", "Vikram",
        "Akhil", "Aniket", "Ashwin", "Chaitanya", "Keshav", "Samarth", "Nirav", "Tanmay", "Tarun", "Vivek"
    ],
    "África do Sul": [
        "Thabo", "Sipho", "Mandla", "Sibusiso", "Themba", "Nkosi", "Lungile", "Xolani", "Dumisani", "Vusi",
        "Andile", "Ayanda", "Bongani", "Hlengiwe", "Lwazi", "Mthunzi", "Nomvula", "Phumzile", "Sanele", "Thulani",
        "Zanele", "Kgotso", "Lerato", "Malusi", "Nkosinathi", "Ntando", "Siphiwe", "Siyabonga", "Teboho", "Tshepo",
        "Zola", "Nkateko", "Tshiamo", "Buhle", "Kgosi", "Nhlanhla", "Sello", "Thandeka", "Mduduzi", "Andries",
        "Lebohang", "Lucky", "Muzi", "Kabelo", "Tumelo", "Thokozani", "Samkelo", "Zandile", "Khanyisile", "Sakhile"
    ],
    "Nigéria": [
        "Chinedu", "Emeka", "Ifeanyi", "Uche", "Ngozi", "Chukwu", "Obinna", "Nnamdi", "Eze", "Amaka",
        "Olu", "Ayo", "Ade", "Bola", "Chioma", "Ebuka", "Femi", "Kelechi", "Kunle", "Tunde",
        "Tope", "Yemi", "Ngozi", "Chigozie", "Nkechi", "Chinonso", "Ogechi", "Ebele", "Ikenna", "Chukwudi",
        "Osita", "Chibueze", "Okey", "Uzo", "Olisa", "Ifeoma", "Obi", "Ada", "Amaechi", "Chukwuka",
        "Nwachukwu", "Ezinne", "Chijioke", "Onyeka", "Ngozika", "Olumide", "Anayo", "Chukwuemeka", "Olubunmi", "Chidiebere"
    ],
    "Egito": [
        "Ahmed", "Mohamed", "Ali", "Hassan", "Ibrahim", "Youssef", "Omar", "Abdel", "Khaled", "Amr",
        "Mahmoud", "Tarek", "Saad", "Ehab", "Walid", "Mostafa", "Ashraf", "Karim", "Sherif", "Fathy",
        "Ziad", "Adel", "Anwar", "Ayman", "Eman", "Gamal", "Habib", "Hisham", "Ismail", "Kamal",
        "Mina", "Nagib", "Nasser", "Nabil", "Osama", "Ramy", "Rashad", "Sami", "Shadi", "Tamer",
        "Wagdy", "Yahya", "Zaki", "Fayez", "Salah", "Sabry", "Reda", "Abbas", "Atef", "Bassam"
    ],
    "Turquia": [
        "Ahmet", "Mehmet", "Mustafa", "Ali", "Hüseyin", "Hasan", "Osman", "Yusuf", "İbrahim", "Murat",
        "Serkan", "Burak", "Cem", "Kemal", "Fatih", "Kadir", "Orhan", "Tayfun", "Erdem", "Sinan",
        "Emre", "Barış", "Selim", "Hakan", "Levent", "Oğuz", "Onur", "Bora", "Volkan", "Zafer",
        "Halil", "Can", "Çağrı", "Yasin", "Rıza", "Erhan", "Tolga", "Cihan", "Efe", "Serhat",
        "Furkan", "Cenk", "Doğan", "Enes", "Koray", "Gökhan", "Arda", "Tuna", "Tamer", "Egemen"
    ],
    "Irã": [
        "Ali", "Hossein", "Mohammad", "Reza", "Ahmad", "Hassan", "Mehdi", "Ebrahim", "Saeed", "Amir",
        "Farhad", "Karim", "Javad", "Majid", "Naser", "Shahram", "Babak", "Sina", "Arash", "Kourosh",
        "Navid", "Masoud", "Pouya", "Hamed", "Shahin", "Mostafa", "Hamid", "Parsa", "Yasin", "Ashkan",
        "Ramin", "Bahman", "Behnam", "Kian", "Keyvan", "Sam", "Shervin", "Vahid", "Farshad", "Nima",
        "Kambiz", "Morteza", "Omid", "Shayan", "Arman", "Peyman", "Mehrdad", "Kaveh", "Shahriar", "Ehsan"
    ],
    "Grécia": [
        "Giorgos", "Dimitris", "Nikos", "Kostas", "Vasilis", "Panagiotis", "Andreas", "Ioannis", "Christos", "Athanasios",
        "Spiros", "Manolis", "Stelios", "Petros", "Elias", "Marios", "Antonis", "Fotis", "Evangelos", "Savvas",
        "Georgios", "Apostolos", "Anastasios", "Lambros", "Michalis", "Alexandros", "Thanos", "Argyris", "Sotiris", "Kyriakos",
        "Theodoros", "Nektarios", "Nikolaos", "Dionysios", "Aris", "Achilleas", "Efstratios", "Konstantinos", "Vangelis", "Kyriakos",
        "Stamatis", "Vassilios", "Leonidas", "Polykarpos", "Makis", "Agis", "Pavlos", "Tassos", "Gregorios", "Miltiadis"
    ],
    "Suécia": [
        "Erik", "Lars", "Karl", "Anders", "Johan", "Per", "Björn", "Nils", "Olof", "Gustav",
        "Fredrik", "Henrik", "Mats", "Tomas", "Daniel", "Magnus", "Andreas", "Stefan", "Joakim", "Kristian",
        "Robert", "Patrik", "Håkan", "Jan", "Jonas", "Axel", "Oskar", "Sven", "Bo", "Emil",
        "Filip", "Elias", "Viktor", "Jesper", "Albin", "Leon", "Gabriel", "Sebastian", "Simon", "Martin",
        "Rasmus", "Anton", "Theodor", "Knut", "Robin", "Alfred", "Jonathan", "Arvid", "Tobias", "Benjamin"
    ],
    "Noruega": [
        "Ola", "Knut", "Hans", "Erik", "Lars", "Bjørn", "Svein", "Arne", "Odd", "Trond",
        "Olav", "Per", "Tor", "Eirik", "Steinar", "Espen", "Kristian", "Sigurd", "Magnus", "Håkon",
        "Einar", "Nils", "Jan", "Morten", "Sondre", "Stian", "Simen", "Petter", "Jon", "Jørgen",
        "Audun", "Geir", "Halvor", "Henrik", "Tormod", "Ragnar", "Are", "Leif", "Frode", "Harald",
        "Vegard", "Asbjørn", "Sverre", "Trygve", "Kjetil", "Øystein", "Andreas", "Alexander", "Åge", "Finn"
    ],
    "Dinamarca": [
        "Mads", "Peter", "Lars", "Anders", "Søren", "Jens", "Rasmus", "Jesper", "Thomas", "Henrik",
        "Nikolaj", "Christian", "Martin", "Jakob", "Frederik", "Daniel", "Emil", "Jonas", "Victor", "Michael",
        "Mikkel", "Magnus", "Andreas", "Kasper", "Simon", "William", "Sebastian", "Oliver", "Alexander", "Philip",
        "Lucas", "Mathias", "Theodor", "Oscar", "Tobias", "Elias", "Benjamin", "Oliver", "Johannes", "Malte",
        "Karla", "Johan", "Adam", "Anton", "Ludvig", "Viggo", "Jes", "Stefan", "Niels", "Erik"
    ],
    "Finlândia": [
        "Matti", "Juhani", "Timo", "Kari", "Antti", "Jukka", "Pekka", "Heikki", "Seppo", "Mikko",
        "Juha", "Teemu", "Lauri", "Markku", "Pentti", "Eero", "Ville", "Jari", "Risto", "Olli",
        "Ilkka", "Tapio", "Sami", "Petri", "Ari", "Kalevi", "Jorma", "Jaakko", "Harri", "Vesa",
        "Kai", "Pasi", "Jouni", "Arto", "Reijo", "Jussi", "Erkki", "Simo", "Raimo", "Esa",
        "Tommi", "Kristian", "Veikko", "Kimmo", "Olavi", "Kaarlo", "Leo", "Niilo", "Paavo", "Anssi"
    ],
    "Países Baixos": [
        "Jan", "Pieter", "Hendrik", "Johan", "Dirk", "Hans", "Willem", "Gerrit", "Cornelis", "Arjan",
        "Rik", "Stefan", "Thomas", "Martijn", "Joost", "Sander", "Luuk", "Daan", "Bart", "Dennis",
        "Vincent", "Casper", "Kees", "Ewout", "Floris", "Harm", "Bram", "Coen", "Niels", "Ruben",
        "Lars", "Maarten", "Jelle", "Jeroen", "Bas", "Koen", "Michel", "Ralf", "Thijs", "Timo",
        "Kevin", "Mark", "Hugo", "René", "Frank", "Job", "Oscar", "Roel", "Tobias", "Max"
    ],
    "Áustria": [
        "Franz", "Josef", "Wolfgang", "Stefan", "Peter", "Heinz", "Klaus", "Andreas", "Michael", "Johann",
        "Martin", "Lukas", "Thomas", "Paul", "Rudolf", "Matthias", "Florian", "Günther", "Christian", "Anton",
        "Georg", "Manfred", "Bernd", "Felix", "Robert", "Karl", "Benjamin", "Dominik", "Philipp", "Herbert",
        "Patrick", "Sebastian", "Norbert", "Markus", "Alexander", "Hans", "Richard", "Leon", "Benedikt", "Leopold",
        "Niklas", "Simon", "Daniel", "Maximilian", "Jakob", "Christoph", "Fabian", "Erich", "Elias", "Jonas"
    ],
    "Polônia": [
        "Jan", "Piotr", "Krzysztof", "Andrzej", "Tomasz", "Pawel", "Marek", "Adam", "Wojciech", "Marcin",
        "Jacek", "Maciej", "Lukasz", "Jakub", "Rafal", "Mariusz", "Mateusz", "Grzegorz", "Dominik", "Karol",
        "Jerzy", "Zbigniew", "Kamil", "Wiktor", "Przemyslaw", "Michal", "Bartlomiej", "Artur", "Dariusz", "Norbert",
        "Sebastian", "Henryk", "Ryszard", "Bartosz", "Kazimierz", "Eryk", "Tadeusz", "Stanislaw", "Leszek", "Czeslaw",
        "Daniel", "Oskar", "Hubert", "Konrad", "Aleksander", "Szymon", "Filip", "Fryderyk", "Igor", "Stefan"
    ]
}

SOBRENOMES_INTERNACIONAIS = {
    "Japão": [
        "Tanaka", "Nakamura", "Yamamoto", "Takahashi", "Kobayashi", "Saito", "Matsumoto", "Fujimoto", "Yamazaki", 
        "Okamoto", "Shimizu", "Kinoshita", "Shibata", "Ishikawa", "Morita", "Honda", "Hasegawa", "Taniguchi", "Ogawa", 
        "Ando", "Hashimoto", "Maeda", "Ueno", "Kuroda", "Fukuda", "Yamada", "Oshima", "Inoue", "Nagata", "Miura", 
        "Kaneko", "Hayashi", "Yoshida", "Matsuda", "Nakagawa", "Ono", "Endo", "Arai", "Imai", "Nishida", "Okuda", 
        "Takagi", "Sugiyama", "Hino", "Miyamoto", "Kawai", "Machida", "Oda", "Morimoto", "Sasaki", "Murakami", "Umeda", 
        "Kameda", "Otani", "Kitamura", "Kurokawa", "Takayama", "Shimada", "Kikuchi", "Okada", "Nakamoto", "Hoshino", 
    ],
     "Coreia do Sul": [
        "Kim", "Lee", "Park", "Choi", "Jung", "Kang", "Cho", "Yoon", "Jang", "Lim",
        "Han", "Shin", "Seo", "Hwang", "Moon", "Oh", "Song", "Jeong", "Hong", "Yu",
        "Ahn", "Go", "Nam", "Baek", "Ryu", "Kwon", "Huh", "Jo", "Suh", "Ha",
        "Bae", "Im", "Yoo", "Joo", "Byun", "Chung", "Yang", "Koo", "Shin", "Son",
        "Min", "Cheon", "No", "Seok", "Bang", "Kwak", "Cha", "Na", "Jeon", "Woo"
    ],
    "China": [
        "Wang", "Li", "Zhang", "Liu", "Chen", "Yang", "Huang", "Zhao", "Wu", "Zhou",
        "Xu", "Sun", "Ma", "Zhu", "Guo", "He", "Lin", "Luo", "Song", "Tang",
        "Deng", "Gao", "Jiang", "Fang", "Shi", "Yu", "Han", "Xiao", "Cao", "Cheng",
        "Hao", "Zheng", "Peng", "Lu", "Pan", "Xie", "Wei", "Yuan", "Du", "Qian",
        "Bai", "Yao", "Nie", "Ding", "Yin", "Fu", "Tian", "Long", "Kong", "Ren"
    ],
    "Estados Unidos": [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
        "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
        "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
        "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
        "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"
    ],
    "Brasil": [
        "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Rodrigues", "Almeida", "Nascimento", "Carvalho",
        "Lima", "Araújo", "Fernandes", "Barbosa", "Ribeiro", "Monteiro", "Melo", "Martins", "Gomes", "Lopes",
        "Rocha", "Dias", "Teixeira", "Moreira", "Vieira", "Nunes", "Freitas", "Cavalcanti", "Castro", "Cardoso",
        "Alves", "Ferreira", "Pinto", "Correia", "Torres", "Farias", "Miranda", "Coelho", "Moura", "Batista",
        "Machado", "Medeiros", "Campos", "Assis", "Fonseca", "Leite", "Andrade", "Soares", "Tavares", "Barros"
    ],
    "Alemanha": [
        "Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Koch", "Richter",
        "Krause", "Schulz", "Hoffmann", "Bauer", "Lehmann", "Schröder", "Schmitt", "Wolf", "Neumann", "Schwarz",
        "Zimmermann", "Braun", "Krüger", "Hofmann", "Hartmann", "Lange", "Werner", "Schumacher", "Seidel", "Engel",
        "Keller", "Brunner", "Hahn", "Lang", "Fuchs", "Kaiser", "Schreiber", "Bock", "Klein", "Walter",
        "Berger", "Dietrich", "Schilling", "Geiger", "Hermann", "Heinz", "Maurer", "Vogel", "Baumann", "Reinhardt"
    ],
    "França": [
        "Dupont", "Durand", "Moreau", "Lemoine", "Rousseau", "Bernard", "Martinez", "Garcia", "Petit", "Girard",
        "Lambert", "Bonnet", "Francois", "Leclerc", "Simon", "Chevalier", "Renaud", "Gauthier", "Legrand", "Noel",
        "Roy", "Blanc", "Garnier", "Perrin", "Marchand", "Lemoine", "Fabre", "Picard", "Muller", "Lopez",
        "Bertrand", "Dubois", "Meyer", "Benoit", "Gaillard", "Henry", "Renard", "Carre", "Colin", "Arnaud",
        "Payet", "Michel", "Barbier", "Hernandez", "Jacquet", "Bailly", "Boucher", "Clement", "Schmitt", "Perrot"
    ],
    "Itália": [
        "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Ricci", "Marino", "Bruno", "Gallo",
        "Greco", "Conti", "De Luca", "Mancini", "Costa", "Giordano", "Rizzo", "Lombardi", "Moretti", "Barbieri",
        "Fontana", "Santoro", "Mariani", "Caruso", "Ferrara", "Rinaldi", "Martini", "Leone", "Longo", "Ferri",
        "D'Amico", "Serra", "Barone", "Sanna", "Amato", "Palmieri", "Monti", "Conte", "Neri", "Gatti",
        "Messina", "Donati", "Battaglia", "Piras", "Orlando", "Ricciardi", "De Santis", "Coppola", "Basile", "Ruggiero"
    ],
    "Espanha": [
        "García", "Martínez", "López", "Sánchez", "González", "Rodríguez", "Fernández", "Pérez", "Martín", "Gómez",
        "Ruiz", "Hernández", "Jiménez", "Álvarez", "Moreno", "Díaz", "Muñoz", "Romero", "Alonso", "Navarro",
        "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Molina", "Morales",
        "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marín", "Iglesias", "Reyes", "Gutiérrez", "Peña",
        "Cruz", "Herrera", "Núñez", "Cortés", "Santiago", "Campos", "Vega", "Fuentes", "Carrasco", "Cabrera"
    ],
    "Argentina": [
        "González", "Rodríguez", "Gómez", "Fernández", "López", "Martínez", "Pérez", "García", "Sánchez", "Romero",
        "Torres", "Ramírez", "Álvarez", "Domínguez", "Moreno", "Muñoz", "Díaz", "Ruiz", "Silva", "Molina",
        "Castro", "Gutiérrez", "Rojas", "Navarro", "Ortega", "Vega", "Rivera", "Ávila", "Medina", "Cabrera",
        "Luna", "Herrera", "Campos", "Maldonado", "Chávez", "Olivares", "Ramos", "Sosa", "Águilar", "Escobar",
        "Núñez", "Cáceres", "Palacios", "Santana", "Reyes", "Páez", "Peña", "Acosta", "Vera", "Arias"
    ],
    "México": [
        "Hernández", "García", "Martínez", "López", "González", "Rodríguez", "Pérez", "Sánchez", "Ramírez", "Torres",
        "Flores", "Gómez", "Vargas", "Jiménez", "Ramos", "Cruz", "Moreno", "Díaz", "Ortiz", "Reyes",
        "Chávez", "Aguilar", "Ruiz", "Gutiérrez", "Castro", "Vega", "Mendoza", "Cortés", "Molina", "Campos",
        "Salazar", "Ríos", "Núñez", "Herrera", "Paredes", "Escobar", "Guerrero", "Domínguez", "Rosas", "Maldonado",
        "Peña", "Valdez", "Barrera", "Aguirre", "Franco", "Zavala", "Padilla", "Fuentes", "Villanueva", "Silva"
    ],
    "Inglaterra": [
        "Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies", "Robinson", "Wright",
        "Thompson", "Evans", "Walker", "White", "Green", "Harris", "Martin", "Wood", "Clark", "Jackson",
        "Edwards", "Turner", "Hill", "Cooper", "Ward", "Carter", "Phillips", "Mitchell", "Parker", "Collins",
        "Morris", "Rogers", "King", "Cook", "Bell", "Lee", "Young", "Scott", "Hall", "Allen",
        "Moore", "James", "Kelly", "Watson", "Bennett", "Morgan", "Bailey", "Reed", "Price", "Marshall"
    ],
    "Rússia": [
        "Ivanov", "Petrov", "Sidorov", "Smirnov", "Kuznetsov", "Popov", "Vasilyev", "Morozov", "Volkov", "Fedorov",
        "Mikhailov", "Nikolaev", "Pavlov", "Semenov", "Andreev", "Alexeev", "Egorov", "Ivanova", "Novikov", "Sergeev",
        "Stepanov", "Orlov", "Makarov", "Zaitsev", "Tikhonov", "Kozlov", "Grigoriev", "Markov", "Frolov", "Karpov",
        "Danilov", "Zhukov", "Belov", "Bogdanov", "Romanov", "Osipov", "Konev", "Malyshev", "Gavrilov", "Tarasov",
        "Nikulin", "Shapovalov", "Polyakov", "Yakovlev", "Sorokin", "Filippov", "Lebedev", "Anisimov", "Ermakov", "Alekhin"
    ],
    "Canadá": [
        "Smith", "Brown", "Tremblay", "Martin", "Roy", "Wilson", "Johnson", "Anderson", "Taylor", "Clark",
        "Moore", "Scott", "Reid", "Young", "King", "White", "Campbell", "Stewart", "Thompson", "Mitchell",
        "Murphy", "Murray", "Williams", "Cooper", "Richard", "Harris", "Jackson", "Green", "Roberts", "Wood",
        "Ward", "Gray", "Bennett", "Fisher", "Lewis", "Gagnon", "Lavoie", "Girard", "Rousseau", "Dube",
        "Bergeron", "Fortin", "Bouchard", "Beaulieu", "Parent", "Simard", "Ouellet", "Lemieux", "Lebel", "Lefebvre"
    ],
  "Austrália": [
        "Smith", "Jones", "Williams", "Brown", "Wilson", "Taylor", "Johnson", "White", "Martin", "Anderson",
        "Thompson", "Walker", "Harris", "Clark", "Young", "Hall", "King", "Wright", "Scott", "Hill",
        "Green", "Baker", "Adams", "Campbell", "Roberts", "Mitchell", "Moore", "Evans", "Carter", "Phillips",
        "Jackson", "Edwards", "Turner", "Collins", "Stewart", "Cook", "Parker", "Bennett", "Cox", "Kelly",
        "Bailey", "Reid", "Ward", "Howard", "Foster", "Barnes", "Watson", "Hughes", "Price", "Wood"
    ],
    "Portugal": [
        "Silva", "Santos", "Ferreira", "Pereira", "Oliveira", "Costa", "Martins", "Gomes", "Rodrigues", "Lopes",
        "Almeida", "Ribeiro", "Carvalho", "Sousa", "Teixeira", "Fernandes", "Monteiro", "Cardoso", "Rocha", "Barros",
        "Pinto", "Vieira", "Melo", "Cruz", "Neves", "Fonseca", "Andrade", "Leite", "Couto", "Castro",
        "Azevedo", "Mendes", "Faria", "Simões", "Henriques", "Moura", "Marques", "Amaral", "Borges", "Morais",
        "Esteves", "Tavares", "Sá", "Figueiredo", "Viana", "Coelho", "Ramos", "Antunes", "Duarte", "Nunes"
    ],
    "Índia": [
        "Patel", "Singh", "Kumar", "Sharma", "Gupta", "Reddy", "Agarwal", "Chopra", "Mehta", "Iyer",
        "Verma", "Pandey", "Rana", "Choudhary", "Thakur", "Rao", "Joshi", "Malhotra", "Bhat", "Nair",
        "Das", "Roy", "Mishra", "Ghosh", "Kulkarni", "Tiwari", "Naidu", "Prasad", "Desai", "Seth",
        "Bhatt", "Kapoor", "Yadav", "Lal", "Chawla", "Shukla", "Bhardwaj", "Dubey", "Kaushik", "Bansal",
        "Pathak", "Shetty", "Vyas", "Singhal", "Sinha", "Bajaj", "Rastogi", "Mahajan", "Rajput", "Kaur"
    ],
    "África do Sul": [
        "Mokoena", "Nkosi", "Zulu", "Dlamini", "Ngcobo", "Khumalo", "Shabalala", "Mhlongo", "Sithole", "Ntuli",
        "Mbatha", "Zuma", "Mkhize", "Mabaso", "Ngwenya", "Mdletshe", "Hlongwane", "Buthelezi", "Cele", "Maseko",
        "Tshabalala", "Msibi", "Nxumalo", "Zikhali", "Magubane", "Nkambule", "Masango", "Manzini", "Mazibuko", "Simelane",
        "Hlatswayo", "Gumede", "Radebe", "Mabena", "Ndlovu", "Mduduzi", "Thwala", "Mtshali", "Ndaba", "Luthuli",
        "Mbatha", "Dube", "Zondi", "Xulu", "Mnguni", "Mavuso", "Nyathi", "Hadebe", "Ngubane", "Ntshangase"
    ],
    "Nigéria": [
        "Okeke", "Okonkwo", "Ibe", "Eze", "Nwosu", "Uzo", "Onyeka", "Anyanwu", "Chukwu", "Obi",
        "Okechukwu", "Ogbonna", "Njoku", "Ezeh", "Nwachukwu", "Onyekachi", "Uche", "Chibuzo", "Ikenna", "Amadi",
        "Iheanacho", "Okezie", "Nwankwo", "Chinonso", "Osita", "Oluwaseun", "Tunde", "Ayodele", "Femi", "Segun",
        "Akin", "Olumide", "Adeyemi", "Olufemi", "Babatunde", "Damilola", "Chidiebere", "Oluwadamilola", "Chinwe", "Ngozi",
        "Ogechi", "Ugochukwu", "Chimamanda", "Ifunanya", "Chidimma", "Chinedu", "Ifeanyi", "Chika", "Ekene", "Kelechi"
    ],
    "Egito": [
        "El-Sayed", "Hassan", "Mohamed", "Ahmed", "Ali", "Mahmoud", "Youssef", "Ibrahim", "Salem", "Omar",
        "Khaled", "Mustafa", "Farouk", "Zaki", "Fathy", "Hussein", "Gamal", "Abdelrahman", "Ashraf", "Samir",
        "Nasser", "Adel", "Sami", "Ehab", "Anwar", "Ezzat", "Morsi", "Shaaban", "Kassem", "Lotfy",
        "Awad", "Radwan", "El-Sharkawy", "Abdelkader", "Fouad", "Hegazy", "Sobhy", "El-Masry", "Shaker", "Tamer",
        "Hany", "Bahgat", "El-Din", "Naguib", "Shahin", "El-Baz", "Saad", "Kamal", "Amer", "Emad"
    ],
    "Turquia": [
        "Yılmaz", "Kaya", "Demir", "Şahin", "Çelik", "Aydın", "Öztürk", "Arslan", "Doğan", "Kılıç",
        "Aksoy", "Aslan", "Gül", "Bozkurt", "Erdem", "Bayram", "Özdemir", "Polat", "Çetin", "Koç",
        "Yavuz", "Uçar", "Çakır", "Taş", "Altun", "Korkmaz", "Baş", "Karaca", "Şimşek", "Kurt",
        "Dinç", "Bulut", "Keskin", "Gündüz", "Erdoğan", "Ateş", "Yalçın", "İnan", "Çiftçi", "Akbulut",
        "Ergin", "Kaplan", "Köse", "Sarı", "Avcı", "Göksel", "Acar", "Bilgin", "Özkan", "Şeker"
    ],
    "Irã": [
        "Mohammadi", "Hosseini", "Ahmadi", "Rezaei", "Alavi", "Jafari", "Karimi", "Gholami", "Shahbazi", "Ebrahimi",
        "Farhadi", "Nouri", "Asadi", "Eskandari", "Rostami", "Akbari", "Rahimi", "Kazemi", "Abdollahi", "Fakhri",
        "Tabrizi", "Bagheri", "Jalali", "Khalili", "Madani", "Zamani", "Noori", "Sharifi", "Yazdani", "Ranjbar",
        "Ansari", "Namazi", "Torabi", "Shojaei", "Etemadi", "Amiri", "Taheri", "Soltani", "Pour", "Sharif",
        "Beheshti", "Mansouri", "Pezeshki", "Zadeh", "Hedayati", "Fazeli", "Sadeghi", "Vahidi", "Saeedi", "Ahmadpour"
    ],
  "Grécia": [ 
      "Papadopoulos", "Nikolaou", "Georgiou", "Dimitriou", "Vasileiou", "Konstantinou", "Ioannidis", "Anagnostopoulos", "Christopoulos", "Theodorou",
      "Pappas", "Karagiannis", "Katsaros", "Tsakalidis", "Alexandrou", "Markopoulos", "Galanis", "Antonopoulos", "Oikonomou", "Koufos",
      "Mitsopoulos", "Samaras", "Voulgaris", "Triantafyllou", "Lykourgos", "Xanthopoulos", "Argyris", "Grigoriou", "Spyridis", "Petrou",
      "Kouris", "Efstathiou", "Giannakopoulos", "Platis", "Zervas", "Lazaridis", "Chatzis", "Maniatis", "Tsoukalas", "Koutoulas",
      "Makris", "Sideris", "Papagiannis", "Kalogeropoulos", "Panagiotopoulos", "Tsiolis", "Zografos", "Vogiatzis", "Skoulas", "Christidis"
  ],
  "Suécia": [
      "Johansson", "Andersson", "Karlsson", "Nilsson", "Eriksson", "Larsson", "Olsson", "Berg", "Svensson", "Axelsson",
      "Lindberg", "Sandström", "Lundqvist", "Lindgren", "Nyström", "Forsberg", "Lund", "Hedlund", "Ström", "Dahlgren",
      "Engström", "Holm", "Wikström", "Norberg", "Åkesson", "Hansson", "Björk", "Wahlström", "Månsson", "Blomqvist",
      "Persson", "Hellström", "Löfgren", "Fredriksson", "Högberg", "Ekström", "Palm", "Wiklund", "Boström", "Norén",
      "Hellman", "Nyberg", "Berglund", "Håkansson", "Ek", "Lindahl", "Hedman", "Strömberg", "Lundberg", "Öberg"
  ],
  "Noruega": [
      "Hansen", "Johansen", "Olsen", "Larsen", "Andersen", "Pedersen", "Nilsen", "Kristiansen", "Jensen", "Karlsen",
      "Moe", "Bakke", "Haugen", "Dahl", "Solberg", "Holm", "Eide", "Foss", "Lunde", "Myhre",
      "Lie", "Sørensen", "Thoresen", "Halvorsen", "Berge", "Bjerke", "Engen", "Ruud", "Tangen", "Rønning",
      "Aasen", "Bråten", "Kleven", "Skog", "Lind", "Nygård", "Svendsen", "Vik", "Krog", "Aamodt",
      "Strand", "Helgesen", "Lindberg", "Fredriksen", "Vold", "Kleven", "Krogh", "Skogheim", "Langeland", "Torp"
  ],
  "Dinamarca": [
      "Nielsen", "Jensen", "Hansen", "Pedersen", "Andersen", "Christensen", "Madsen", "Larsen", "Rasmussen", "Sørensen",
      "Poulsen", "Thomsen", "Mortensen", "Olesen", "Knudsen", "Eskildsen", "Lauridsen", "Skov", "Bertelsen", "Kjær",
      "Mikkelsen", "Simonsen", "Dam", "Holm", "Lund", "Bonde", "Bach", "Aagaard", "Jepsen", "Hermann",
      "Krog", "Gade", "Vestergaard", "Lind", "Brandt", "Brogaard", "Dalgaard", "Hougaard", "Holst", "Vinther",
      "Ravn", "Hald", "Leth", "Birk", "Thorsen", "Bisgaard", "Høgh", "Ager", "Klitgaard", "Bentsen"
  ],
  "Finlândia": [
      "Korhonen", "Virtanen", "Mäkinen", "Nieminen", "Heikkinen", "Koskinen", "Järvinen", "Lehtonen", "Hämäläinen", "Laine",
      "Pitkänen", "Aalto", "Kinnunen", "Savolainen", "Räsänen", "Ojala", "Leppänen", "Salminen", "Turunen", "Tuominen",
      "Pietilä", "Väisänen", "Koivisto", "Mattila", "Kuusisto", "Vuori", "Kärkkäinen", "Niskanen", "Rantanen", "Pohjola",
      "Seppänen", "Luoma", "Peltonen", "Eskelinen", "Kallio", "Koskela", "Väänänen", "Holopainen", "Nousiainen", "Suominen",
      "Mustonen", "Hyvönen", "Hakala", "Mäkelä", "Ahonen", "Hietala", "Vartiainen", "Takala", "Lepistö", "Rautiainen"
  ],
  "Países Baixos": [
      "de Jong", "Jansen", "Visser", "Bakker", "Smit", "de Boer", "Kok", "Bos", "Peters", "Hendriks",
      "van Leeuwen", "van Dijk", "Meijer", "de Groot", "Koning", "Dekker", "Post", "Kuiper", "Schouten", "van Veen",
      "van der Meer", "Mulder", "Boer", "Timmermans", "Veldhuis", "Verhoeven", "van Dam", "Snijders", "Blok", "Peeters",
      "Lammers", "van de Velde", "de Wit", "Veenstra", "Molenaar", "Kamp", "Brouwer", "Vries", "van Loon", "Hoekstra",
      "Smits", "Hoogendoorn", "Bongers", "Jongbloed", "Scholten", "Kouwenhoven", "Rietveld", "Verbeek", "Hogendoorn", "Groen"
  ],
  "Áustria": [
      "Müller", "Huber", "Bauer", "Wagner", "Gruber", "Steiner", "Schmid", "Leitner", "Berger", "Hofer",
      "Fischer", "Moser", "Schwarz", "Lang", "Weber", "Winkler", "Auer", "Koch", "Haider", "Egger",
      "Lechner", "Mayr", "Brunner", "Pichler", "Reiter", "Schuster", "Baumann", "Maurer", "Hofer", "Wallner",
      "Eder", "Zimmermann", "Schmidt", "Kern", "Jakob", "Linder", "Riedl", "Albrecht", "Brandstätter", "Lorenz",
      "Seidl", "Fuchs", "Pfeifer", "Hafner", "Friedl", "Trummer", "Wimmer", "Oswald", "Gasser", "Weiss"
  ],
  "Polônia": [
      "Nowak", "Kowalski", "Wiśniewski", "Dąbrowski", "Lewandowski", "Zieliński", "Szymański", "Wójcik", "Kozłowski", "Kwiatkowski",
      "Krawczyk", "Mazur", "Jankowski", "Kubiak", "Piotrowski", "Sikora", "Adamski", "Czarnecki", "Nowicki", "Sobczak",
      "Grabowski", "Ostrowski", "Chmielewski", "Wroblewski", "Błaszczyk", "Pawłowski", "Kamiński", "Kaczmarek", "Król", "Wilk",
      "Baran", "Michalski", "Zakrzewski", "Wysocki", "Borkowski", "Górski", "Wieczorek", "Zawadzki", "Rutkowski", "Piątek",
      "Szulc", "Skowroński", "Janik", "Stępień", "Szczepaniak", "Lis", "Nowosielski", "Gajda", "Urbaniak", "Kaleta"
  ]
}

