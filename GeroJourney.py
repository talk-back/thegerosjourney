print('''
*******************************************************************************
  _______ _                _____                _               _                                   
 |__   __| |              / ____|              ( )             | |                                  
    | |  | |__   ___     | |  __  ___ _ __ ___ |/ ___          | | ___  _   _ _ __ _ __   ___ _   _ 
    | |  | '_ \ / _ \    | | |_ |/ _ \ '__/ _ \  / __|     _   | |/ _ \| | | | '__| '_ \ / _ \ | | |
    | |  | | | |  __/    | |__| |  __/ | | (_) | \__ \    | |__| | (_) | |_| | |  | | | |  __/ |_| |
    |_|  |_| |_|\___|     \_____|\___|_|  \___/  |___/     \____/ \___/ \__,_|_|  |_| |_|\___|\__, |
                                                                                               __/ |
                                                                                              |___/  
                _.-''|''-._
             .-'     |     `-.
           .'\       |       /`.
         .'   \      |      /   `.
         \     \     |     /     /
          `\    \    |    /    /'
            `\   \   |   /   /'
              `\  \  |  /  /'
             _.-`\ \ | / /'-._
            {_____`\\|//'_____}
                    `-'

*******************************************************************************
''')
shells = 0
input("La oscuridad es absoluta y el frío te envuelve como si te amara. Una frase te resuena en la cabeza: 'Presiona Enter para continuar'. ¿Qué crees que signifique?\n")
input("Estás en una especie de playa en un ddía invernal y, evidentemente, perdido. Aunque prometiste ya no hablarte así, no puedes evitar sentirte estúpido.")
input("¿Qué clase de idiota se pierde en una playa? \n")
while True:
    camino = input(
    "El autodesprecio no te va a salvar de esto. Enfócate. ¿Hacia dónde quieres ir? (Opciones: Izquierda, Derecha, Atrás, Arriba, Adelante)\n¿De aquí para dónde?:\n")
    if camino == "Izquierda":
        shells += 2
        #CGI OLAS
        input("""                                                                                                    
                                                                                                    
     :~~:                     ..........                                                            
     .~~.                ...::..... ..::^^....                                                      
     :^^..            ....          :~^^..:::....                                                   
  :: :^~:.         .:..    .    :~^^^^^^^:^~^^:^~:                                                  
  ^^ : ~~.      ..:.    ..^^~Y?!!~?PP#?:~::~^^^^^^.                                                 
  !~ ^!~~.    ::..     .:~!7!G&&#PGB@@#Y!:^:^:..^...::..                                            
  ~~ ^~^~.  .^.       !GY#P&@B@@@@@&@@#&PJ7Y!.^:^:..^^^::                                           
  ::      .:.         ^&@@&@@##&&#@@&&&&@@G7:^~:~^^:^:..:^.                                         
.     .:::.            :?Y?YGBB@#&&###&#&#P!.^~^^^~.:^^~^ ..                                        
5Y5YJ?7^.    .  .^     :.  ^7P&#GG###&&BG^ . .^^^:^^::~~^:                                          
PP?~:      .^:.^~:..: :~:^~.~?!!5GB&#@&#^     ..:. .^::^::.                                       ..
   . .^^.^?Y^  :~:!^^:^!::^~~..^~~!75#&B.           ..:.:                                      ...  
   ^~^^~:^5@BPG7. !~^:^BG5PGBJ?^:!P&B&@Y                                                     ...  .:
 ^~^^77:~^!JPB#P^^^~.  ^~7~G&B&GJPG&##&G.                                                   ..   .:^
:^7J!7BPBGJB#BBJ~^~!JY~^:^~JBB@#BP&&B#B#J                                              .:.~:   ..^~Y
:.7Y?:!JP&&#&BBP!P#GB##J!JPPB&BBP!!YYP##G5.                                          :7!^^.   :^^Y#&
:^.::^ ^~?JPG##&##BBB#&#&BGBGBG?     .:7B&G^                                      ^?YB5^.    .^^!B@@
^^:^^:  :!!~7JYPBBB&@#BB&##G?~.         .JB#!. .     .         ..       .  .....!5BPY!.    ^?YP&&#@&
:.JP7?!JP?!7!~~~~~7J5YYG#BY!.    .:^.    .~?55?~!!~~~!~!!~^^^...::.:^^^^~~^^^::~Y?!^...::JJG@@@#GY!^
  G@#PGG&#P?777!!~JGYJ!...     .:^~^      .:..~:~???JYJJ???~:~. ..:~7??7!??7~:::    .:7YYGBPYJJ7.   
  .?PPBBB##G?~^~7^^!~.     .^  :~^^^.:: .:  :^:^  ^!J5PPPPY7?GP?5PJ?JPGY^^^::::~~7??57!!^:~!J57.    
     .::^:..       .    .:.~^^^:~.:..^:^^Y7:  :7Y^:?~:~??5PGP5P5YYJJ?77!^^~~~.!YJ?!^::!?YYJ!:    !5B
           .:     .^^ .. .:.:^.   .:^.:G7?Y7~~!^?#P?GJ~55~   ....     ...::..   ~!?YYPBBJ~ ^!!YPPB##
    .:.:~^::. .P!:^^.:^:  .  ^:^:^:^:. YBPY!~YG7^^?YG@&GPBG?:    ::    ^~~~^!??YPB##BY^    ~J55PG55Y
   .~7^^7JJ?~?5&G^^:::::: ~:.:~^^^^~:^ .P&&&P!!JJ??7!JPB#GB&&GJ!:~J5YJ~!JYPGPPPPBBP7:  :^^7YPPPPGGPG
  7G&&5YGB##BGPY!^^!!~^.^.^^^~.:GYGJ7~. .?&@@@BY!~~!7?J?777?Y5GBBPYJYP&#GGG#P#P!^. :^^!JY5PP5YYGB###
 7@G&PJG#&#GBP~?BB5B##J7 ^:.:   75PP&J!Y: :JG@@@&P?~^::^~^      .:^^^!!??J7!^^::::7B&@@@&&&#BGB###&@
 5&&BB##P&###&#BB&&###@G  .^PG^^!P~7P#G&&!^. ^?P#@@&B5?7!!77~~~!!!!~:.::.:JYPB#&&&#GP5?~^::.     ..:
~#G##&#@##&#@@B&###B&&#P~7?P??^?J7^:777P&##Y!!...~!7J5PPPPP5Y?7!~^..      :^~~~^^::.                """)
        input("\nLas olas del mar rugen violentas junt a ti. La espuma te acaricia la cara después de cada estallido de las olas. Es una caricia llena de ternura, profecía y amenaza. Mejor quedarse en la orilla...\n")
        continue

    elif camino == "Derecha":
        shells += 1
        #CGI DUNAS
        input("Una enorme duna se alza a tu derecha. El viento va soplando la arena, desgastándola poco a poco, pero a menos que te sobren miles de años para esperar a que termine el proceso de erosión, esta no es una ruta viable.\n")
        continue
    elif camino == "Atrás":
        input("\nComienzas a sentirte extraño luego de voltear hacia atrás. Te miras las manos y ves cómo se cristalizan, cobrando un color blanco parecido a... sal.")
        #CGI TORBELLINO OPCIONAL
        input("\nLa marea comienza a agitarse aún más y el rugido de las olas se parece cada vez más a un grito. Antes de que tus oídos también se conviertan en sal te parece escuchar: 'Te lo dije. En repetidas ocasiones, TE LO DIJE.\nJamás. Miras. Atrás.'")
        input("""⠀⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠄⠀⢀⣠⣤⣤⣤⣤⣤⣤⣤⠀
⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⢋⣤⣾⣿⡿⠿⠛⠋⠉⠉⠉⠉⠀
⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣷⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⣿⣿⠟⠁⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣶⣶⣤⠀
⠀⠘⣿⣿⣿⣿⣧⠀⠀⠀⠀⢸⣿⠋⣀⣤⣾⣿⠛⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⠀
⠀⠀⠈⢻⣿⣿⣿⣧⡀⠀⠀⢸⣿⠟⠉⠀⣈⠙⢿⣶⣄⡀⠀⠀⠀⠉⠛⠿⣿⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣷⣄⠀⢸⡇⠀⠀⠀⢘⣧⠀⣿⣿⢿⣦⡀⠀⠀⠀⠀⠈⠀
⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣦⣸⣧⣄⣀⣠⣾⡟⢀⣿⣿⡌⢻⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⣿⣯⣭⣴⣿⢻⣿⡇⠀⢻⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡿⠁⣾⣿⡇⠀⠈⣿⣿⣷⡀⠀⠀
⠀⣿⣶⣦⣤⣤⣤⣤⣤⣤⣤⣶⣾⣿⣿⡿⠋⠀⣰⣿⣿⡇⠀⠀⢸⣿⣿⣷⠀⠀
⠀⠈⠉⠉⠙⠛⠛⠛⢋⣩⣽⣿⣿⠟⠋⠀⢀⣴⣿⣿⣿⠁⠀⠀⠈⣿⣿⣿⡇⠀
⠀⣤⣤⣶⣶⣶⣶⣾⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⡏⠀⠀⠀⠀⣿⣿⣿⣷⠀
⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠛⠛⠛⠛⠀""")
        input("""\n  __                  _            
 /__  _. ._ _   _    / \     _  ._ 
 \_| (_| | | | (/_   \_/ \/ (/_ |  
                                   """)
        input("""\n  __                  _            
 /__  _. ._ _   _    / \     _  ._ 
 \_| (_| | | | (/_   \_/ \/ (/_ |  
                                   """)
        input("""\n  __                  _            
 /__  _. ._ _   _    / \     _  ._ 
 \_| (_| | | | (/_   \_/ \/ (/_ |  
                                   """)
        break
    elif camino == "Arriba":
        shells += 1
        #CGI CIELO
        input("El cielo tiene el color de una televisión sintonizando un canal muerto.")
        input("""⣿⣿⣿⣿⣿⣿⣿⣛⣻⡻⣷⣦⣙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⣴⣾⣿⣿
⣿⣿⣷⣾⣾⠿⡯⣿⣿⣿⣪⢿⡿⠿⣶⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣹⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣾⣿⡔⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⣼⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠿⣻⢟⠟⢻⡆⠿⢿⣿⡿⢛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡰⣾⣿⢟⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣭⣭⣽⣯⣯⠜⣻⠿⢿⠿⢟⣛⣛⣛⣩⣽⣒⡿⢿⡿⠷⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣴⣿⣿⣿⣶⣙⣛⣭⣴⣶⣌⣛⣛⣛
⣿⣿⣿⣿⣿⣿⠿⣛⣵⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣐⣪⠻⣿⣿⠟⢫⠶⠶⣬⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣭⣥⣭⣭⣭⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠈⣭⣾⣿⣿⡘⣡⣾⢆⣭⣽⣹⣟⠙⢨⢴⣒⠲⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠚⡀⠘⠾⢵⣙⣻⣿⡿⢃⣿⣿⣿⣿⣿⣿⢩⡶⠦⢄⢺⡇⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⢄⠀⠏⢗⣒⣛⣿⣷⣾⣿⣿⠿⢟⣻⣿⠿⠚⠄⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣒⣠⣚⣞⣮⣧⣴⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⢻⣻⠻⢿⣿⣿⣿⠿⠏⡴⠬⢍⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠣⢨⡝⢻⣿⣆⠟⠩⠚⠻⢻⢛⣞⡙⠲⠄⣶⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿
⣿⣿⣿⣿⢘⠪⢹⣙⣐⣒⣾⣿⣿⣿⣿⣿⣶⣶⣾⣿⣼⣶⣌⢹⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⣈⣬
⣿⣿⣿⣿⣜⢶⣘⢀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⡆⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢻⣫⣼⠾⣹⣶⣿
⣿⣿⣿⣿⣿⣶⣜⡲⢜⢶⢌⣹⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⠟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⡰⠶⢾⠷⠶⠪⣍⣍⣴⡶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣮⣤⣔⣒⣚⣛⣟⣻⣛⣛⣭⣵⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣓⣊⣟⡋⣼⡶⣣⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡡⢶⠤⠼⠭⢯⣷⣷⣿⣿⣴⣿⣿⡿⡿⠿⠿⢟⣛⡛⠿⣿⣿⣿⡿⢋
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢛⣛⣛⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⢰⣶⢪⡭⣠⢨⣤⣤⣀⡈⢓⡜⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡀⢴⠊⢠⣶⣦⡰⠻⠻⢿⣻⣿⢿⣿⣬⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣢⣾⢸⣿⣿⣿⣿⣿⣿⣿⣟⣟⣟⣟⠯⠴⡔⢉⠛⠿⠿⠿⢟⣛⡛⠿⢿⣿⣿⣿⣿
⠿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⡩⢠⢚⣒⣋⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⠿⢿⣷⣷⣷⣿⣷⣶⡸⣶⡏⣿⣷⡮⠹⢿⣿
⣝⣣⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⡾⣸⣷⣾⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣋⠇⠜⢟⡛⡿⡿⡟⣸⣿⣶⣛⣫⣽⠰⣾⣿
⣯⣭⣛⣓⣊⢭⣛⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⡨⢼⢨⢯⢷⢿⣮⠦⠼⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⢃⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣶⣦⣰⣽⣛⠿⣿⣿⣿⣿⣿⣿⣧⣐⢲⠤⣴⠵⠷⢖⣒⣒⣋⣴⣾⣿⣿⣿⣶⣶⣭⣝⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⡺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣬⣭⣭⣭⣭⣭⣴⣶⣿⣿⣿⣿⣿⣿⣿
⣛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣛⣻⣩⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣶⣬⣽⣽⣭⣬⣽⣭⣿⣵⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
        continue

    elif camino == "Adelante":
        #CGI CAMINO EN PLAYA
        input("""              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^""")
        print("Sigues hacia adelante\n")
        break
input("¿Eso que está ahí es una ostra gigante?\n")
input("Wey, no mames, sí es una ostra gigante.\n")
input("Al acercarte te das cuenta que se mueve, como si abrirse\n")
input("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&B5YY55555GB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GP@#@@&#GPPPGGGPGGGB&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P75G&@@@@@B!~~~~~!!7?5GB#&&#&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PB@@PB@@@@&&B~^^^^^^^:^:7B&##BBBBB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@57G@@@@@@@@@@@@J:^^^^^:::!#@Y~~!?Y5GPYP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#PPB@@@@#&@@@@@@7::::^^::.5@@B!~^^^^~7Y5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BYY&@&&@&B#@@@@@@&?.::::::.^J&@@#J~^^^^^^^~J#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GG###&&###@@@@@&&!::::::::?#@@@@B~~^^^^^^^^^~Y#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@&&#&&&&@@@@@@@#P?!!::::::::7J?BB@@&?!~~!!~~^^^^^~?P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@&B#B#@@@@@&#B5!^::^^^^::::::~~!??@@&!?7!777?7~!^~^^^!JG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#B&GG#&@@@BJ!!~~::::::^^^^^^^^^^^~7~G@@#!!J~7P77Y7^~~^^^^^^!5@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGGB@@@&5!^::::^::::^!!!Y57!!~!?JJP&@@#Y~^~775JJ??7~^^^7!~^J~#@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@YP&5G&@@B!^::^^^^^::^J#&&&@@&&&&@@@@@@BYJJ!^~777!~^~~~^~^~7??B!^YGB&@@@@@@@@@@@@@@@@@@@@@@@
&@@@@@@@@@@@@@@@@@@@@@@@@@@B7?#&&GB&&!^^^^^^^^^^JB@@@@@@&&#BGPY?777~!~!~??^^~!!~~^^^~~^^^!Y?::::~!?5G#@@@@@@@@@@@@@@@@@@
&@@@@@@@@@@@@@@@@@@@@@@@@@B~7YB&#G&@P^^^^^^^^^!B@@@#GY?7!~~^^^^^^^^^~^~7#?^~^~~^^^^~^^~~^^~^~^^^^::::^!?5PB#&@@@@@@@@@@@
@@&&@@@@@@@@@@@@@@@@@@@@@@YBB7!5BP@@P^^^^^^^^?&@@#J~^^^^^^^^^^^^^^^^^~~J?~^~~^~~~~^^^^^^^^PBGJ~^~!!~^::::::^~!YGB####&&&
@&&&##@@&@@&@@@@@@@@@@@@#PB@5^~?PP@@#J^^^^^^!&@@@!^^~^^^^^^^^^^^~~!7Y5^^^~^^~~~^^^^^^^^^^!BY!J?JGG??YJJ5?~!7!^^^^^^^~~~!
5G#@&&@@@@@@&@@@@@@@@@@#5B@#7^^7Y&@&?~^^^^^:P@@@Y^^^^^^^^^^^~??YPJ7777^^^^^!7~^^^^^^^^^^~YY!?G&@&#G#@@@@&####5YPYP5Y?77!
!^~?YP#@&#B&@@@@@@@@@@GY5@@J~~~JG@&?^^^J~^^^#@@G^^^~^^^^^^^^^^^^^::^^^^^^~!~~~^^^^^^^^~^?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
YY5PBB&&BBB&@@&#&@@@@&YB@@G~77!B@@J^^^~7^^^P@@&?^^^^^^^^^^^^^^^^^^^^^^^^~!~^^~^^^^^^^^^7&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@&#G&@@@@@&@@#Y!7YB@&?^^^^~^^^Y@@@PY~^^^^^^^^^^^^~~^~~~~~~~~~^^^~^~^^^^~~^!&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@&GYJ5&@G!^^^^^^^^~&@@&JJ7^~~~^^~^^^^^^^^~~~~~~^^~~^^^^^^^^^~^^G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@GGBGBG&#7^^^^^^^^^^!@@@&GJJ!~~~~^^~~^^^^^~~^^^^^^^^~~~^^~~^^^^^5&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@BJB&@&PJ!^^^^^^^^^^^G@@#YPY!~^^^^^^^^^^^^^^^^^^^^^^^^^~^^^^^^^^Y#G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&?P&@B!^^^^^^^^^^^:^P@@&?!~77~^~^^^^^^^~~~^^^^^^^^^^~^^^^^^^^^^YB5#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#?B@#!^^^::^^^^^^~J#@@B!^^^^~~!!^^^^^^^^~~^^^^^^^^^^^^~~^^^^^~!G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@B&@Y^~^^^^^::^7P#@@#J~^^~^^^^YY^^^^^^^~^^^^^^^^~^~^~~^^^^^^^5#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@
@@@@@@@@@@@@@@@@@@@@&B@@?^^^^::~?P&@@&G?~^^~^^^^^!P7^~~^^~~~~~^^^^^^!~~^~~^^^^^~!~5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@&&&@@@@@@@@@#P@@P^~^^!P&@@#P?~^^^~^^^^^7557~^~~~^~~~~^^^^~^^^^^^^^^^^^^!!^^5&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@##@@&&&&&@#JY@@B~^^Y&@@P7~^^^~^^^^^^^!P57^^^^^~~^^^~~^^^^^^^^^^::^^^^~7!?YP#B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@&G@#&&&@@@#&&@&@P~P@@&~^G@@#7^^^~^^^^^^^^!~~~^^^^^^^~^^^^~^^^^^^^^^^^~!~7577PYY&@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@&@@@@@@@@@@@@&&J?B@@P^P@@B~^~~^^^^^^^^^^^^^^^^^^^^^^^^~^^^:^^^^^^~J5#&BG#BGB##@@BP&@#GG&@&@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@B?B@@7!@@@7^~^^^^^^^^^^^^^^^^^^^~^^^^^^^^::^^JY!^~75&@@@&@@@@&@@@@&@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@BYJP@@P^Y@@#~^^^^^^^^^^^^^^^~~^^^^^^^^^^^^:^~??J5PJP#B&@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@&&@@@@@@@5~J#@@G~^B@@5^~~^^^^^^^^^^^^^^^^^^:::^^^^^^^!755G#G&#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@
@@@@#B@@@@@@@@@@PB@@&5^:7@@@7^~~^^^^^^^^^^^~^^^^:::::7P5P7~PBP#&&##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GYY~Y@@@@@@@@@
@@@@&&@@@@@@@@@#&&B5!::^G@@G^^~~^^^^^^^^^^^^^:^^~7JG5B#?5BB#&@@@@&&&BG@@#B&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P^^^~#@@@@@@@@@
@@@@@@@@@@@@@@&57!~^^^:?@@@7^^~^^~~^^^~^^^^^^~JPB##@@@@&@@@&@@@@@@@@&&&#&BB&&@@@@@@&@@@@@@@@@@@@@@@&@@BG?^~^^5&GG#@@@@@@      """)
#CGI OSTRA GIGANTE

while True:
    concha = input("\n¿Abres la ostra? Y/N\n")
    if concha == "N":
        input("Sigues tu camino y dejas atrás a la ostra gigante. Eventualmente, también sales de la playa y regresas a tu vida. Una vida completamente normal, ordinaria, aburrida incluso. De vez en cuándo sueñas con la concha gigante y su contenido. Te alejaste de ahí pensando que tal vez sería algo peligroso, y probablemente lo fuera, pero la oportunidad de contemplar la belleza no se presenta todos los días y tu castigo por haberla dejado ir es vivir una vida sin ella.\n\n\n")
        input('''                   _,,,_
                 .'     `'.
                /     ____ \
               |    .'_  _\/
               /    ) a  a|         .----.
              /    (    > |        /|     '--.
             (      ) ._  /        ||    ]|   `-.
             )    _/-.__.'`\       ||    ]|    ::|
            (  .-'`-.   \__ )      ||    ]|    ::|
             `/      `-./  `.      ||    ]|    ::|
            _ |    \      \  \     \|    ]|   .-'
           / \|     \   \  \  \     L.__  .--'(
          |   |\     `. /  /   \  ,---|_      \---------,
          |   `\'.     '. /`\   \/ .--._|=-    |_      /|
          |     \ '.     '._ './`\/ .-'          '.   / |
          |     |   `'.     `;-:-;`)|             |-./  |
          |    /_      `'--./_  ` )/'-------------')/)  |
          \   | `""""----"`\//`""`/,===..'`````````/ (  |
           |  |            / `---` `==='          /   ) |
           /  \           /                      /   (  |
          |    '------.  |'--------------------'|     ) |
           \           `-|                      |    /  |
            `--...,______|                      |   (   |
                   | |   |                      |    ) ,|
                   | |   |                      |   ( /||
                   | |   |                      |   )/ `"
                  /   \  |                      |  (/
            jgs .' /I\ '.|                      |  /)
             .-'_.'/ \'. |                      | /
             ```  `"""` `| .-------------------.||
                         `"`                   `"` ''')
        input("""  __                  _            
 /__  _. ._ _   _    / \     _  ._ 
 \_| (_| | | | (/_   \_/ \/ (/_ |  
                                   """)
        input("""  __                  _            
 /__  _. ._ _   _    / \     _  ._ 
 \_| (_| | | | (/_   \_/ \/ (/_ |  
                                   """)
        input("""  __                  _            
 /__  _. ._ _   _    / \     _  ._ 
 \_| (_| | | | (/_   \_/ \/ (/_ |  
                                   """)
        break
    elif concha == "Y":
        input("Levantas la concha y es tan grande que abrirla requiere de todas las fuerzas de tus piernas y brazos. Cuando por fin la abres, te das cuenta que al centro hay un hombre desnudo hecho un ovillo.")
        input("""::::^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~~!!!!~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^::::::
^^^^^^^^^^^^^^^^~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^
^^^^^~~~~~~~~~~~~!!!!!!!!!!!!!77777!77!!!!!!!!!!!!!!7777777777777777777777777777!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~^^^^^^
~~~~~~~!!~~!!!!!!!!!77777777777777777?77777777777????????????????????????????????????77777777777777777!!!!!!!!~~~~~~~~~~
!!!!!!!!!7777777777777??7????????????????????????JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ????????????????????77777!!!!~~~~~~~
!!777777777????????????????JJJJ???J?JJJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYYYYYYJJJJJJJ????????????7777777!!!!!!!!~~~~~~!!
77777???????????????JJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJJJJJJJ????????J?JJJJJJJJJJJJJJ?JJYYYYY
77??????????????JJJJJJJYYYYYYYYYYYYYYYY5YYYYYYY55555555555555555555555555555555555555Y55555555PPPPPPPGPPPPPPPPPPPP555555
??????JJJJJJJJJYYYYYYYYYYYYYYYYYY5555555555555555555555PP55PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP55555555555555
JJJJJJJYYYYYYYYYYYYY55555YY5555555555555555PPPPPPGGGGPPPPPPP5PPP55555PPPPP5YYJJJYYPPPPPPPPPP55555555555YYYYYYYYYYJJJJJJJ
JJJYYYYYYYYY55YYYYY55555555555555PPPPPPPPPPPPPPPPG5YJJ????JJJJYY5555J??JJJY5YJ?7!!7?JY55555555555555YYYYYYYJJJJJJJJJ????
JYYYYYYYYYY55555PPPPPPPPPPPGGGGGGPPPPPPPPPPPPGGGPJ???J???777JYJYPPP55Y???YGBG5PY??JJJYY5YYPPYYYJYYY5PPPPPP5PPPPP5PP55555
YYYYYYYYY55PPPPGGGGPGGGGGGGGGGGGGGGGGGGGGGGGGGPY77??JJ5B5J??77??JJJYYYYJJJ55YJYPGBB#BBG5YJ????J????!7?PBGGGGGGGGGGGGGGGG
YYYY555555555555PPPPPPGGPPPPGGGGGGGGGGGGGGGBG5?7~7?5PJYGBBGGP5YJJ?77??JJ???JYPGBB#GY!^:........::::^^:^PGPPPP55555555555
555555555555PPPPPPPPPGGGGGGGGGGGGGGGBBBBBGP5YJJ7!!JGYJPB&&&#BBGP5YYYYYYY55YP#&&#P7:   ...::::::::::::::YGPP55YYYYYYYYYYY
5555555555PPPPPPPPGGGGGGGGGGGGBBBBGGBBBBY???J5P57JPY75GB#&&&##BBGPPPPGGGGGPGGGY~.    ....:::::::::::::::JBGGPPPPPPPPPPPP
55555PPPPPPPPGGGGGGGGGGGGGGGGGGGBBGGGBBJ!7?J5P5Y5PY7YGBB###&&##BGP55555YJ7!~:.        ...:::^^^:::....:.:GBGGGPPPPPPPPPP
5555PPPPPPPPPPPGPGGGGGGGGGGGGBBBBBGGBBG7!!77?JYGPJ!?PGBB##&#B57^:... .                ....:::::^^^^:::..^GBGGPPPPPP55555
55PPPPPPPPPPPGGGGGGGGGGBBBGGGGPP55YYYYY?!!~!!JPY7~75GBB##BY!.                        .....::::::::::::..~BBGGGGPPPPPPPPP
PPPPPPPPPPPPPGGGGGGGGGGPPP55P555YYYYYYYY?!~^!7!~7?5GBBB5!:                            ....:::::^::::::::.?BGGGGPPPPPPPPP
PPPPPPPPPPPPGGGGGGG5J?7!7J555555PPY??????7~~~~!Y5YPGGY~                               ..........::::::^::^GGGPPPPPPP5555
PPPPPPPPPPGGGGBBGYJY5PPPGGGGPPGGGY7?J?77?J?7?YYPBP5?:             .::.                ....:::::::........!GGGPPPPPPPPPP5
PPPPPPPPGGGGGG5J~75GGBBBBBGPPGGJ77??5B5JYGBPG#G5J~.              .Y5P7:               .....:::::::::::::JBGGGGGPPGGPPPPP
PPPPGGGGGGP5YJ?!~YPGPGGGGG555G7~!?YP5PGGGGPY?!^.                 .YG577.              ....::::::.....:.:PBBGGGGGGGGGPPPP
PPPPPGGGPJ?JYYY77YPBGBBGG5YYP?~?YPPGGGGP?~.                 ..::::!PY~^.              ....::::::::::....^YBBGGGGGGGGPPPP
PPPPPGGP!7J555Y!?5PBBBBBGJYP5!75GGGGPJ~.                  .^~7JPPPGB5~...            .....::::::::::::::.^PP5555Y555YY55
~~!!!!!~~Y55PP577Y5GGBBGG?J55YY5555?~.                    ~!YG#####BBP?7?J7:         .....:::::::::......:~77!~^:^~~^^^^
!!!~~^^^??JY5PPY!7YPPGGGG??YPPPP5J7^.                    ^7JJ7B###B##BBGPYGJ.        ....:::::::::::::::::.^?Y5Y!~^~~~!!
~!77????!^?Y5PGGJ!JPGGGGP?7J5PP55J~.                    ?BP!.~PPP5B##B5?^.!!:.        ...::::::::::::::::::.!??JJ?????JJ
?!~^!7JY?~7JY5PGPJYPGGGBPY!J5PP5J!:                    J#5~..7BP5PG5J7^  .^!~:       ....::::^^^^::::...::.:5GGPY5YJJJYY
JYY7!!?Y5JJJJY55P5YJYY55557!YPPY7^.                   ?&Y:  :P#BPGP?^.    .75~.       ....:::::^^^^^^^:::::!!~~!??J5PGPP
..^7!!!?JJYY???JY5PJ7JY5PPY:7557~.                    J&Y.  :PBBGBPJ~:     !#P^       ...::::::::::::^^^^7YYJ7!!~~~~7J?7
!~!7!7!~^?JYY?7?JY55J7JPPGJ:7YY!^.                    7&Y  ...^~!!^:..     Y#B~       ...:::^^^^^^:::..:YBGGGGPPPP555555
?5?77J??~!!7J5Y7!7J5PYJPGGY^Y5Y!:                     ~#J .~?^...^!?J~.    ?#P:      ...:::::^^^^^^^^:::~YBP5P5PGGBGPPP5
YY7!!??JJ?7!!7?YY?!7YPYJPP77PP5?:                     :B5^7~PJ:.J##B5!.    ~#Y:     ...::::^^^^^^^^^^^^^::7!!!7!77??7?JJ
7:.:~~!????J?!~!?JYJ7?YYYG~7GGPY~.                    :5J7Y?~!^~#&#BP!.    :G?.     ....:::^^^^^^^^:::::::~~~7J????7??77
:~~^~~^~!!7JYYYJ?77?YJJY5GJJGBBPY~.                    ^!!JP!^:^B&#B5~.    7P~. . .....:::::^^^^^~~^^^^::^~~~~!~~^^^:...
?YPY!7!!~^!?JY55555YJJJY57^JBBBBGY~.                     ~YP?:. 5##GY^.   .Y5^ ...:^^~!~~^^^^^^^^^^^~~^^^:.....  .......
#BBP!!!??!~!7?JJY55555YY?~~?BB#BBG5?^                    ~JP!.  ?#GP!.    .~7::~!7JYYYYJ?!~~~~^^^::::^^~^::::::::^^:::::
!^::^~~7??!^^~!!?JYYY55Y?!!?BBBBBBBG57:   ......         :7J^.  YGGY:....::!?JYYYJYYYJJ??7~~^^^^^^^:~7!!!!!!~~!!!7777777
   ..^^^7??7!~^^~~7?JY5YJ!~^Y#####BBGG57:...:^^^::...     .::.  !5G?.^!!7???7~^:.....:^^~~~^::^^^^:^JY??77!!!!!!!77?????
.....:^^^!77??7!^^^~!!!7!~^^:7P###BBBBBG5?!~^~~~~~~~^^^::.....  .5P?:~~^::.  ..:^^^:.....:::::::::.^YYJ?7!!!!!!7!7??777?
~~~~~!!!^:^~~~777!~^^^:::::::.:!5B#BBBBBBGGGGP5Y5PPPP55PP5Y7^.  ^GGJ:    ..:^!~^^::^^^:......:....:?YJ??777???77??J?7777
????JJY5J~^::::^^~~~^^^::::::.. .~YGBB#BBGGBBBBBPPGB#BGPPGGGPJ~..5P?. ...:~~^.       .::........:~7??7777???J?????777777
~~~~~!7JJ?~^::..........:....      :!?5PGGGGBBBBGPPGGGPP55PPGGGY!J5~...:^~:             .........:::::::^^^~~~~~~!!!!!!!
777777???!7?77!!~^^^^^:::::...         .:~!!777!~^^::.....:~7YPGGYY^.:^^.                                           ....
77777??J!~~!!!7?YJ??77!!!!!77~^^^::....                       .^7?Y^::......................................::::.::^^:::
!!!!7777!77!!~!!!!77777777?J5YYJ7~~~^:::......   ..   .:^^:::::::!J^::^^^~~~!!~~^:^^^^^~^^^^^^^~~~!!77777!77?J?77???7!!!
!!~~~~~!77!!!!!!!!!!!!!!!!!!!7?JYPYJ?JJJJ???77!!~^~!~~7JYJ7!77777!!!!~~~~~!!!!!!!777?777??J?777777??????JYPGBPP5YJ??!!!!
!77777!!77!!!!!!!777777??JJJJJJJYGP!!!!77777???JJ?7???JY55555JJJJJJJ????JYYY555YJ?JJJJJYYYYYYYJJJJJJYYJY55PP5J5J??77??7!
^~~~7?JYJJ?77!!7?Y?!7?JJJJJJJJ???7!!!!7!!!!!!!!77??JPPPP5Y5YJ??JJYYYYYYPGGPP5PPP5YYY555PPPP555555YYYJYYYYYYYJJJJ??JJJJ??
~~~~~~~!!7!!!!!!??!!!!!!77777?777777777????????JJJJ5P55555555YYYYYY5555PPPPPPPGGGGPPPPPPPPPPPPP5555YYYJJJJJJJJJ?????J???
!!!!!!!!!!!7!!!777777?77777??JJJ??JJJJYYYYYYYJJYY5YJ555J?JY55555555PPPP55PPPPPPP5PPPPP555555555YYY5YYYYJJJ???????7777!!!
Y!7!!!!!!!777YPPPPJ!!7?JJJJJJ??J?JJ??JJJJJYY555YYYY5PP5YJYY5555YY555PPPPPPPPPPPPPP5YYYY555YYYYYYJJJJJJJJ????777777777777
J75J7!!7777!7Y555YJ?~~~!7J?JJ?JJJJJJJJYY555PPPPP5555Y555555555555555555Y5PPP555PP555YJJJJYYYJJJJJ??7777777????777777!!!!
~~??!!!!7777??7??777????JJYYYYYJJJJJJYYYYYJJJJJJJJJJYYYY5555YY5555YYYYYJ??JYYYYYYYJJJYJJ????????????????7?7777777!!!!!!!""")
        break
    #CGI VENUS SALIENDO DE LA ESPUMA PERO ES GERO
    else:
        input("Solo puedes elegir Y o N, perrevergue")
        continue

input("Te acercas con cautela y notas que su piel azulada tiene un filme viscoso encima. Su cabello es del mismo verde que el de las algas y está tan rizado como algunas de ellas. Acercas tu mano a su piel escamosa y, cuando estás a punto de tocarlo, despierta\n")
#CGI DEDOS TOCÁNDOSE
input("""&#BG#BG55?~~!!!7!7^::.....:::.:::::~?7JYY7!~:^^!J?7?J7:?G7Y^.:^!~^!?7YGP55JJPGBB
#BPPBGP5Y7~!77~~~~:~^:::..~7^~^^:.:7?7??!~~^^:.^^7?!~7!!YYY~^:!~:~~~75P5GP5PPBGP
#B5YP5GPY???7!!~!^7^::::.:~!~7!::.:!~~!~~^^^~:...:~^:~7JY?!!7J?!7~!7PBGGGGBGPGGG
GBGPPGP55YYJ?7!?~^~:...::!^!~!~:::!Y~~!~^~!!J!~^:~!::!7Y!:^~?!JY?7PBBBGGGGGGGP5P
GGBGGBPGPYYJJ7??:::....^~~~^:::.:~JPJJ?YYJ?!7J??J?J?!~~J7~7?~~~555BBPB#BPGGPGP5P
BPGGGBGPP55J?7?!^~:.....^!~~~^::::~7JJJYYJ~~:^^^~~~^...:!^7J!^~YGGPGGGBBBBBGBPYP
GPPGGGGPPYJYY?7^:~:.....:~~^^^^^^::^^~~~~!~7^:^^:^J:.:.^^.:7:^!PBGBBG5BGPBBBBPPG
YPP5PGPG5J7?Y?!:...:::..~^^^~^:^~^^~~77!7JJJJJ?77?Y~.::?^::~~!?GBBGGPG#5GGGGGBGG
JPPGGBG5PY??!7~:.~^.::::!!!7?!~!!775555Y5J7!^~~!~~~YJ!77Y7^^!7YBPP55P5555GPPG5GG
5YJP5GBG5?7~^::.......^^::^~?77!^^:!?JJJ?7~7~.:::~JJ^::::!?55J5GPGBGPP5PGP5?PYYG
GGPYJJ5J7~~^:...:....:^^::.:~?7!~^^:^!~J!!7?PJ??J?57:^.::^~PB5PBGBBPY5BBG5YP5P5G
#BBGPPPY?~:..:..::...^^^~~::^!!~!??!7YJJYYPYYPJ^^^!?~.:7^:~YBJ5PBBBBBGBGGBBGPGBB
####BBBBG5!::^::^^^^~?~~!!!~J5J7!!!JGGY?J7!7JYY7^:~~Y?7Y7!77555PBGGBBBGPB#BGYGBG
#######BBP?^^:::^~^::.:.!7!.77~^^^^7YYPJJ?7^!~!YPY7~~7^:~PYJ!J55GGBBB#PBBGGP5GGB
&######BGG5^^::..^!~~^:.:!~:.:~~~~~^~!77777Y?7Y?J7...^^.:J7!?!5P#GGBGGGBBBPBBGGG
&&&&####BBJ:~::::.!~?!::.Y^:!.~~~!7?7~!77?5YYYY::~^..:::^!~J757JPYPPGBGBGB5PGGGG
&&&&&&&#B5~~!!!^^75J7!!7?GJ!7!75YP555557^?7!7JP?~!!~~^^~~~!57YY~?PGG5PGGGGGBBBGG
&&&&&&B5?!!~~~!~7P?~::::^?7~?!!P77?YJJ?7^7!!!??7??JY5::..^^!?YJ~!5G5Y5PPPGGBBGG5
&&&##GJ~~!~!J?~!^.!~::^^:~J7:~P7^^^~!~~!^?!~~7!^77?7~~:....~?J??!?P55PPGPGBBBBGG
###BY7~^~~.~??7~!.^7~!!^:~Y?^^5!7:~77?7!?5J77?^.:~::~!?^...:!YYPY!YGGPPBGPBGPBGB
#BGY!!!~~~!^:75Y5?!Y57~^~YG5J?Y?77?J5PGGBYY?~7~ .::^?YY?^:.:.~?Y55J5YPG55GPGGBBB
#GY!~~^~~!?7J?PP55!:::...:J777?YJ!^:!JGGP5PJ^~~ .::~77JJ7!^:.:~?YJ?YP555PGPGBBGB
PG5?7~^?7^~~?G#BBY:..:^::^7!~!Y5!:!^:?J?7J?7?^!^ .:^~!7J7!^::..~?YJ55P5J5BPYGP5P
^^^~~^^J77BG?P#GBJ:::^~^^!^7Y??7!:^^:!!!JYY5YJ?!..:~^~~!!!!~^: :!JJ5PPGYJPYYY55P
?~.:.:777JPYGB#PP7.:~7~^^^^^!PP!^..::^7?J5JJJY~^:  .^^^^~?Y?^~:.^?YJBBGP5Y5B?PP5
5J!^^^!PPJYP#&BY7.::!J?~^:!77J?~^:.::^!7777Y77!^.:7YY?:.~7?Y?^~??7YPPGY?5Y5GJPY5
Y5?!^^!PGPBP55J7~^:...:^^Y555P7!!:  .:::^~^?!!!^~P#&&#P~:!7YY~^7J555Y5555Y5JJY?J
P555~^7?BG5J~?7!!:.:::.::!?J?J~::..^~!::~!~~:.^^~5G##BB5.^~!?7!~YB555?5YJY5?55YP
5Y555J?75PY!..:~!..::::.!??J7!^: ?GB&&B!.:^..!5BBBGPGGP7.::~!7!^?G5YY55YYP55PPPP
5P5GPP5J?557:...^.:::^~~7!!!7!!!.J##&@&B?:..~B#&&&#P?!:....:^~7^~P5PG5?55J7YGPGB
PP55PPYYYPPJ^:....:::!777!~~JB#&P.7B###BB5^..5B#&&#BY!::....:^^^^YPPJ7???JYYPPB#
YPG5YPPPPGPJ^^:.....:^~~~~^~5&&&#J.!GB####P:.!PGB###GY7~:...:^!!~Y5J?5JJ??P?JPGB
PPP5YPPP5555!^:::...:^!!7~~~Y#&###Y:JGBBBBG7^!Y5GBBBG555J^..::^!~?5JY5Y5GYJJY5BB
5YJP5PPPPP5G5!~:.:^:^~~??~!77GB##B5!JPBBBG5JY?J5BBG55PPPY?7^.::^~!YYPP5PG77Y5PPG
YPPG5YGGGPGGPYJ~^..:^^!7~^!??YPYJG!?JYPPY5YYJJGGBP5Y5PP5GGP57^:^^!YPGGPPPY?JPYJP
YP55YPGPPYPP5555!:.:^!5Y!!77??JYYPPPJJGYY557?YYPP5YY55GPB#GGG5YJ7Y5GGGPP5555PP5Y
55GPP5YYY5G5JYJYY!77!!7!7J7JJYJGP5GY?5YJ55PY5P5PGGBBPGPGG#GBPJ5GBBBBGBGGPGGJ5555
P555PJ?GGPG5P5555J!^!JY?JJPG5Y55YP5JGPP5PYPG5GPPGGB##GPG7JYPPYY5PGP55BGGGBBGG5G5
JYY5GY5JJYPPPPY5PYY7^75YJYGGP5PPGGPBPPPG5J5GGGGPGB#G5Y55?5GP555GP55PY5PGGGGBGPPP
?P&GPY77PBG55555JP5YJ!J57?YBBB#BBGGP55Y5YPGG55PBGPPJ5PYGPPPPPBGYYGYY5YPYPGGBBGPG
5GBJY?YGGPYP55GP5Y5BGPYYJ??Y5BGPGGBGPYJJYBP5PGBBGGPPP5GPPGBBBGP5GG5PP5Y7Y5PP55GP
5YYGP5P55J5GYYYPGPPGBBBP5BP5J5YPPYPBPPP5PPJYP5BB5JJ5PPPPGGGB55YY5PGPPPPP55PBPGG?
JYPPPP5P5PPGGJJGGGPP5PGPGP5YPPGP55YYYPPJ5PP55GGGPPGPPPPYGG5P5PGBBGGGP55PY5BBBPPP
YGPGPPGGYPGGJ7PGYY?PPGGY5P5Y5YPGGPYG5PGPPGPG5PP5555GGYYPPGGPPPB#GGBBPPPBB#BGG5PG
YGG5PYPPPPPGP5BP5YJ5PPGGP55PGPGG55BYYGGGGP5YY55GBPPGGBGGGGBGPBGGYGBGGGBBBBB##Y55
5PGGP5G555YP5555PPP5JPGPG5GBBPPP5PYY5PPG5YY5PGGPPPP5GGGBBBGPBBGBBGGGGPGGPBGGB55P
P7YP5PP555J5Y55GP5GPGGGPGGGGPPPPGGGPPGGY5GBPPGGBBGJPGGBBBBBGGGGBPPBBBGBGGBPBG5GP""")
saludo = input("No seas menso, ¡dile algo!\n")
input(f"Te escuchas a ti mismo diciendo '{saludo}' y la criatura reacciona mirándote con una profunda curiosidad. Sus ojos amarillos reflejan más sorpresa que temor.\n")
input(f"La criatura abre cada vez más la boca y te apartas pensando que te morderá, pero al final solo estalla en carcajadas\n")
input(f"'¿Cómo que '{saludo}'? ¿Y YO soy el que lleva 500 años sellado en una ostra? Hay que salir más, chiquis'.")
input(f"Te quedas mirándolo con la boca abierta y él te mira de vuelta, con una sonrisa inquietante\n")
#CGI SIRENO HERMOSO
input("""####BGP55YJ?77!~^^::....::::::.....:::::::::::::^^^^^~!!!7777?JYYYY5PPPGGGBBBB#######&&&&&&&&&&&&&@@
####BGP55YJ?7!!!~^::.....::::::.....::::::::^^^^^^^^^^^~!!!!77??JJJJYY55PPGGBBBB#######&&&&&&&&&&&@@
####BGP55YJ?7!!!!~^::......::::::...::::::::::::::::^^^^~~!!!7777????JJYY55PPGGGBBB######&&&&&&&&&&@
####BGP5YYJ?7!!!!!~^::......::::::....:^!7??7!~~^:::::^:^^^~!77777???JJYYY55PPGGGBBB######&&&&&&&&&&
###BBGP5YYJ??7!~!!!~~^::.....:::::..:^?5GBBBBBBGPY!::::::^^^^~!77????JY555PPPPGGGBBBB#####&&&&&&&&&&
##BBBGP5YYJJ?7!~~~!~~~^:::....:::::^!^^7GBGB&&&&&&#5^:::^^^^^^^~~!?Y555PPPPPGGGGGGBBB######&&&&&&&&&
##BBBGP5YYYJ??7!~~~!!!~~^^:::..:::^^^^~7G###&&&&&&&&G~:::^^^^~^^^^!?JY5PPPPPGGGGGBBB########&&&&&&&&
###BBGG5YYJJJ??!~~~~!!!!~^^^::::::YPPGP5PB#&&&#####&#P~^^~!!~~~~^^~~!7?JY55PPGGGBBBBBB######&&&&&&&&
###BBBGPYYJJJJ?7!~~~~!!!!~~^^^::::^YPB#BBGB#&&&&#####BG5J77??777!!!!~!!7?Y5PPPGGGBBBBBB#####&&&&&&&&
####BBGP5YYJJJJJ7!!~~~!!7!!~^^:::~Y55555PGB#&&&&&&&&&&#BG5555YJYY!~~~!!!7?Y55PPGGBBBBB######&&&&&&&&
####BBGP5YYYYJYYJ7!!!~~!77!!~^^::J#GGGBB###&&&&&&&@@@&&#GPYJJ?7?J5!~J7!!!7JYY5PPGGGBB#######&&&&&&&&
####BBBG55YYYJYYY?7!!!~~!77!!~^^^PBBGBBB###&&@&&&&@@@@&&&#BGP5JY55J!?57777?JJJY55PGGBB#######&&&&&&&
####BBBGP5YYYJYYYJ?7!!!!!!777!~~~5GBB#&&&&&&&&&&&&@@@@@&&&#######BGP5Y??????JJJJY5PGGGBB######&&&&&&
####BBBGG55YYYYYYYJ7!!!~~!!777!!!!77??Y&&&&&&&&&@@@@&&&&&&###BBBBGPP5YJ?????JJJJJY5PPGGBBB#####&&&&&
#####BBBGP55YYYYYJJ?7!!!~~!7777!!!!!77^G&####&&&@@@@@@@&&&&&&&&#BBBGPPJ!7???JYJJJY5PPPGGGBB######&&&
#####BBBGGPP5YYYYYJJ77!!!!!77?777!!~^..~#&&&&&&&&&&@@@@@@@@&&&&&&&#GBB??JYYY5555YY55PPGGGBBB######&&
&#####BBBGGPP55YYYYJ?77!!!!!77?77!:...!5G##&&&&&&&&&&&&&&@@@&#B&&&&#GP5YYYYYY55PP55555PGGBBBB#####&&
&&#####BBBGGPP555YYYJ?7777!!!7??7~!7!^!5BB##&&&&&&&&&&####&&&&&&###&#BGP5PBG5Y55PPPPP55PGGBBB#####&&
&&######BBBGGPPP5555YJ???7777???7JP5J!7YGBB##&&&&&&##BGGPPB#&&&@@&&&#BBBGPGBYYY55PPPPPPPPGBBB####&&&
&&&######BBBGGGPPP555YYJ???????JJB#G??J5GBBB#####&#BGP55Y5PB#&&@@@&&&&BB#BGPYYYYY55PPGGGGGGBB####&&&
&&&&#######BBBGGGPPPP55YYYYJJJJJJB&G7YPPGBBBB#####BGP55Y5PGB#&&&@@@@&&####BPJ555Y555PGGGGGGBB##&&&&&
&&&&&&######BBBBGGGGPPP5555YYYJYYY##PGGGBBBBB#####BGGPPPPGB#&&&&&&&&&&&&###G5B5YY555PPGGGBBBB###&&&&
&&&&&&&&#####BBBBBGGGGPP55555YYYYJP#BGGBB##BB###&#GGGGGBB#&&&&&&&&&&&&&&&&&&&#PYY5GGGGGBBBBB####&&&&
&&&&&&&&&#####BBBBBBGGGGPPPP55555YG&&B#####B####G5555PGB#&&&&&&&&&&@@@&&&&&&&##BBB####&&&#B#####&&&&
&&&&&&&&&&######BBBBBBGGGGPPPPPP5P#&&&&&&&&#&#G5YYYYY5GB#&&&&&&&&&&&&&&&&&&&&&###&##BBBB&&######&&&&
&&&&&&&&&&&######BBBBBBBGGGGPPPPPG&&&@&&&&##B5555555PGB#&&&&&&&&&&&&##&&&&##&###&&#BGGGGB&####&&&&&&
@&&&&&&&&&&&#####BBBBBBBBGGGGGGGPG&&&&@@&&#P5PPGGGGB#&&&&&&&&&&&&&&###&&&&&#GGBBB##&#GGB#######&&&&&
@&&&&&&&&&&&&#######BBBBBBBGGGGGGG#&&@&#P5YY55PGB##&&&@&&&&&&&&&&&&#B#&&&&&&#GGGGGGB&B##########&&&&
@@&&&&&&&&&&&#######BBBBBBBBBBBBG#&#P7!JPBBBBGB#&&&&&&&&&&&&&&&&&&&#BB#&&&&&#BGGGGG#&B##B#######&&&&
@@&&&&&&&&&&&&########BBBBBBBBBBB#P!!JPGGBB###&&&#&&&&&&&&&&&&&&&&&&BGB#&&&&&#GGBBB#&B##########&&&&
@@&&&&&&&&&&&&&########BBBBBBBG5JJJ5PPPPGGBB##&&#&&&&@@@@@@@&&&&&&&&BGBB#&&&&&BGBBB#&###########&&&&
@@&&&&&&&&&&&&&&########BBGP5J??YPGGBB###&&&&&&&&&&&&&@@&&&&&&&&&&&&BGBBB#&&&&&BGBBBBB#BBB######&&&&
@@&&&&&&&&&&&&#&&&###BP5YJ?JYPGB##&&&&&&&&&&&&##&&&&&@&&&&&&&&&&&&&&BBBBBBB#&&&&BBBBBBBBBB######&&&&
@&&&&&&&&&&&&&###BGP55Y5PG##&&&&&&&&&@@@@@&&&&&&&&&&@&&&&&&&&@@@@&&&BBBB#####&&&&BGBBBBBBB#####&&&&&
@@@@@@@&&&#BGPP5YYYPB#&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&@@@@@&&&###&&&####&&#BBGGGGBBB####&&&&&
@@@@@@@&&#BBPPP55PG#&@@@&&&&&#&&&&&&&&&&@@@@&@&&&&&&&&&&&&&&&@@@@@@@@@&&&&&&&&&&&&&&&&&&&###&&&&#&&&
@@@@@@@&#B##&BB&&&&&&#BGP55?!?JJP55GBBB#&&#&&&&&&&&&&&&&&&&@@@@@@@@@@@&&&&&&&&&&&&&&&&&&@@@@@@&&&&&&
@@@@@@&&&&&&#&@@&&&#BBBG5Y77~~~^!~!?JYY5GB##BB#&&&&&&&&&&&@@@@@@@@@@@@@@&&&&&&&###&&&@@@@@@&&&@@@@@@
@@@@@@@@@&@&@@@&&&&&&&&&BGPGPYYPJJ???YJYYPGPGBB#&&&#&&&&&&@@@@@@@@@@@@@&&&&&&&&&&&@@@&&&&&@&&&&&&&@@
@@@@@@@@@@@@@@@@@@@@@@@@&&&&##&&#BBP5P5PPPGBBGB#B&&#&&&&&&&@@@@@@@@@&&@&@&&&&&&@@@@@&&&&&&&&&&&&&&&&
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&##&#B##BBBB#&&&#&&&&&&&&@@@@@@@@&&&&&&&&@@@@@@@@@@&&&&&&&&&&&&&&&
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&@&@&@@@@@@@@@@&&&&@@@@@@@@@@&&&&&&&&&&&&&&&&&&&@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@&&&&&&&&&&&&&&&&&&@@@@@@
&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
G#G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&#&&&@@@@@@@@@@@@@@@@@@@@@@@@@
&&G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&########&&&@@@@@@@@@@@@@@@@@@@@@@@@""")
nombre = input(f"'Bueno, no te quedes ahí parado. Al menos dime cómo te llamas, para conocer al poeta creador de «{saludo}»', dice entre risas\n")
input(f"'Mucho gusto, {nombre}. Yo soy una nereida y evidentemente no te daré mi nombre porque la última vez que le di mi nombre a un muchacho acabé sellado en esta cosa.'\n")
nereida = input(f"'Pero hagamos algo, como agradecimiento por venir a verme te dejaré elegir mi nuevo nombre. \n¿Cómo debería llamarme, {nombre}?'\n")
input(f"'{nereida}...', dice la criatura mientras saborea el sonido de su nuevo nombre. 'Tal vez no estés tan perdido después de todo, {nombre}\n'")
input(f"'La verdad es que estoy obligado por leyes arcanas a ofrecerte algo a cambio. Pero la verdad completa es que, aunque no estuviera atado a esas leyes, lo haría de todas maneras. Estás lindo, {nombre}', dice y te acaricia la mejilla con una mano húmeda y escamosa.\n")
input(f"'¿Ofrecerme algo como un deseo o algo así?', le preguntas. (,,>﹏<,,).\n")#ASCII SONROJADO
input(f"'¡Absolutamente no! Nada así de directo o vulgar', te responde ofendido.\n\n")
input(f"'La cosa está así, {nombre}: Si ganas, te ofrezco el contenido original de esta ostra en la que estamos. Si pierdes, me relevas aquí adentro por un rato. Tú decides cómo quieres jugar.'\n")
#CGI OFRECIENDO MAGIA
input(f"'Puedes intentarlo directamente y, si tienes la suficiente magia dentro de ti, la bendición es tuya. De lo contrario, tú te quedas en la ostra por 500 años a ocupar mi lugar'.\n")
input(f"'La otra opción es una trivia normal de la vida. Ya sabes, mierda regular de esfinge. No es que yo sea una esfinge, pero alguna vez salí con uno y se pegan algunas mañas'\n")
while True:
    game = input(f"'¿Entonces que será, {nombre}?' ¿Magia o Trivia?")
    if game == "Magia":
        if shells >= 2:
            input (f"La criatura posa su palma sobre tu pecho y te mira a los ojos. Sientes cómo te ruborizas y de pronto eres consciente del ritmo de tu respiración.\n")
            input(f"Finalmente te dice: 'Ok, {nombre}, efectivamente hay más dentro de ti de lo que parece. La bendición es tuya\n")
            input(f"'Lo que había originalmente adentro de la ostra era esto', dice mientras esculca entre sus branquias y saca una perla negra del tamaño de una pelota de golf.\n")
            #CGI Corazón
            input(""" BBGPP5YYJJYYY5Y55PGGBBBP5Y?Y&B##GB@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#GGPP55PBGPPPPPPGGPPPGGBBB##&&&&@
##BBGP55YJ?JJJJJY5PB#BPPP5J!J##&#P#@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@#P555PYYBG5PPPPPPP5555GB###&&&&@@@@
##BBBGPP5YJ?77???J5GBBGPYY?!^7#&&G5#@#B&@@@@@@@@@@@@@@@@@@@@@@@&PYYY55J?B#555555YJJ?JYGB&@@@@@@@@@@@
@&#BBBPPPP5?7!!777?JY5PGPY?!!~!B&#PP&&GB@@@@@@@@@@@@@@@@@@@@@@&5?JYY???YBGP55YJ???7?5G#&@@@@@@@@@@@@
@@@&&#B555P57!!!!!!!!!!?YYYJ?7!7G#5YB@BG#@@@@@@@@@@@@@@@@@@@@#YJJYJ77?JJ555555YJJ??5B&@@@@@@@@@@@@@@
@@@@@@&PY5PP?!~!!777!!!777?J?77!!5B5?PBB##@@@@@@@@@@@@@@@@@@BYJJ????777JY555YYJ?77?5B#&@@@@@@@@@@@@@
@@@@@@@&YJYPY!!7??7!!!7777?JYPP5YPB&P!7YGB#@@@@@@@@@@@@@@&GY??777?7~!7?JYYYY5PPGGBGPGB&@@@@@@@@@@@@@
@@@@@@@@B?J57~!7!~~~~~~~!!7??JPBGGB&&5!!7?J5B&@@@@@@@@@BJ!~~~~^!77!77777????JYY5PB&BYB@@@@@@@@@@@@@@
&&&&&&@@@Y?7~!!~~~^^~^^~!!7JYYPB#B#&@#57!7?JYG#&@@@@@G7^^^^^^:^7777!~~~~~!!77??JYYPBBG#@@@@@@@@@@@@@
@@&&&&@@@Y~!!!~~^^~^~~~7?JY55PG#&&&&&&#Y?JJJY5PB#@@@P^:::::^^:~??7!~^^^^~~~~!!77?JYYPBB#@@@@@@@@@@@@
&&&&&&@&J~!!~^^^^^~~!!?JY5PGGB#&&&&##&&B5YYYY55GB#PB7^^::::::^7JJ7!~^^^^^^^^~~~!77?JY5PG#&@@@@@@@@@@
&&&&@@B7~~~~~^^^~~!7?J5PPGBB#&&&&####&&&GPPP555PBBBB7^::::::^~75Y?!!~^^^^^^^^^^~!!!7?JY5PG#@@@@@@@@@
&&@&BJ~~~~~~!!~!77?JY5PGB###&&&######&&&#BGPP55PGBB#J^::^^~~~!755JJ?7!~~^^^::::^^^^~!7??JJ5PB&@@@@@@
@#5?~~~~~!77?YYJJY5PPGB##&&&###BBB##&@&&#BGPPPPPGBB&Y^^^^^~!!7J5GP55Y?77!~^^:::^::^^!77777??J5G&@@@@
P!!~^~7?J?JY5PGPPGGGB##&&&&#BBBBBB#&&&&&##BGPPPPGBB&Y^^^^^~!7?J5PBBGPYJJ?7!~!~~^^^^~?!7!!!~!?YPB&@@@
7!!~^7?YY5PGGB######&&&&###BBBBBB##&@&&&##BGPPPPGBB&Y~^^^^~!7?J5PGB#BP5YJJ????7!!!7J?7?!!~~7J5GB&@@@
7!~^!?YPGGBB#&&&@&&&&&&###BBBBBB##&&&&&&&#BGPPPGBBB&Y~^^^^~!7??J5PGB#BGP5YJJJJJJY55B5J??!!!?Y5PB#@@@
7~^~?Y5PGB#&&&&&@&&&&&####BBBBB##&&&&&&&&##BGPGBB##&P7~^^^~!77?JJYPPPB#BGP55YY5PB##&&GJJ7!!7?J5GB&@@
!~~!?YPB#&&&&&&&@@&######BBB###&&&@&&&&&&#BBBBBBGPPG57!~~~~~~!7?JJY55Y5PBBGGPP5PP5G#@BP5J!!!!?YPB&@@
~~!7?5G#BB&&&@@@@&#######B####&&&@&&&&&&&##G5?7!~!!7?JJYYJ?!~~!7?JJJYYJ?JP###BBBGGGB#&&PJ7!!~!?5PB&@
~~!7JYGBG#&&@@@@@&###########&&&@&&&&&&&&BJ!~~^^~~~!7?JY5PGGPY7!!7?JJJYYJ7?P#&#BGPPPGB#G!!!!~!?Y5PB&
!!7?JYG#&&&&@@&&BGGG#######&&&@@&&&&&&&&57!!~^::::^^~~!?JY5PGBBP7~!77?JYY5YJYB##BGPYY5GG!!!!~!?Y5PB&
~!7J5B#&&&&@@&&&&&&&&&&&&&&&@@&&&&&&&@&Y7!~^:.    .:^^~77?Y5PGB#&Y~!~~?JJJJY55B##BBBBGPP?!777!7J55G#
77777JYG#@@@@@&&&&&&&@@@@@@@@@@@@@@@@@P?7!^.        :^~7?JJ5PGBB#&Y!???!!!777?YPB#BGGGB#PJ??7!7JY5G#
YY?7!7?YPB&@@@@@&&&&&&&&&&&##&&&&&&&&#Y?7!~:..    .:~!!?YY5P5JPB#&B~!77!!!!~~~~~!7?J5PGY!~~~!?Y5PGB&
P5Y?!!!?YPB&@@&&&#BGGGBBBGGGGB#&&&###B5Y?77!!~~^^~!777?JYPGG?:7PBBB7~!!!~~~!!!~~~~~^~~~~^~!?YPGB#&&@
#BP5Y?!7?5G&@&##BBGGGG#&&BGPPB##&##BBB5YJ?J????77?JJJJY5PGGGJ^!!YG5YJJ??7!!7?7~~!!!~~!7~~7YPB##&@@@@
&&&#GY7~J5G#&&#BBGGGGB#&&#B5PB#&##BBBBGYJJYYYJJJJY55PPPP5YJP5Y7!YGPBGP5YJJJYY?!!!!~^~7~!YB&&&@@@@@@@
@@@&J!!7YG#&&@&#BBGBBB#&&&G5PB#&##BBGGBBP5YYYYY55P5J??!~^:^7JJY5PG#&&##BPYY55J7!7?777!!YB&&&&&@@@@@@
@@@@G7?YP#&&&@@&#BB####&&#GGB#&###BGGGB#&BP55YY55557^^^^^~!7?J5PB&@@@@&&BGGBPYYGP?7~77?PG#&&&&@@@@@@
@@@@@5YG#&&&@@&#GPPPGB&#BP5J?777???JYJJ5P5YY5PPY?7777?JJYYY55PB#@@B5YYJYY5PGPYJY77?JJ55GB#&&@@@@@@@@
@@@@@&B###&@@@@B5YJJYY?!~^^^^~~~!7J5GBY7!!!~~7Y55555PPPPPGGB#&@@B?^^~~7JPGB##BP5YYPB#&###&&@@@@@@@@@
@@&&&&B7?B@@@&57!~~~!~~!!7?Y5555PPG##&&B7~^~!!?YP#&&#BB##&@@@&#G~^~!!?YG#&&@@@@@&##&&&&&@@@@@@@@@@@@
GPPPPGP7?PB#BPJ??7777?JY5G#&&BB####&&&&#P5YYPPG###B?!!7??JPP?!~7JJY5G#&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@
YY555P5YYPGBBGGGPPGBBBB#&&#####&&&&&&###BB###&&#&&&B5JJY5Y~^^~7JGB#######&##&&&&&&&&&&&&&@@@@@@&&###
7777JY5B##&&&&&&&&&&&&&&&##&&&&&#######BB#####&&&&&&#####?!?YPB####&########&&&&&&&&&&@@@@@@&##BGGPP
J?7?JY5GB#&&&&&&&&&&&&##&&&&&&&#########&&&&&&####&####&&GPB###BB###&&&&&&&&&&&@@@@@@@@@@@&#BGGP5YYY
JYPPGGBBB#&&@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&#BBBBBB##&&@@&&@@&&########&&&&@@@@@@@@@@@@@@@&&#BBGPPYJJ?
?7?JYPBB#&@@@@@@@@@@@@@@&&&&&&&&&@@@@@@@@&&&&&#B###&&&@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@&&##BBGGPPYJ?7
7??JY5PPPGGB&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&##BBBBGGGGP5J!?
YJ!~!!!?YPBB##&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&####BBBBBBGGGPGGGGGG57~J
@@#GYJJ?777?YG#&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&###BBBBBGGGGGGGGGPGGGP5PP5555555PPGGGY!~Y
@@@@&#BP5YJ77!7?Y5GB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGP55YYYYYYYJJJJJJJJJYYYYYYYYY5555555PPPPY~!5
@@@@@@@&#BGP5YJ?7?Y5PGB##&&&@@@@@@@@@@@@@@@@@@@&&#BBGP55YJJ??777777????JJ????JJJYYY5P5PGPPPPGGP57^?G
B@@@@@@@@@&&#BGPYJYPGBB#B#BB##&&@@@@@@@@@@@@@&#BGPP5YYJ??777!!7777????JJJ?JJJYYYY5Y5GBBBBBBGGG5J~~YG
PBP#@@@@@@@@@@&#BPYYPGB###&&&&&&&&&&@@@@@@@&#BGP5YYJJ???7777777??????JJJJJJJJY55Y5YPB####BBBG5?!~?PB
##P#@&&@@@@@@@@@@&BP5PB###&&&@@&&&&&&&&&@@&#BBP55YYYYJJJJJJJJJJJJJJJYYYY55YYPPPBGGG##B###BBGPY?!~YGB """)
            input("Es mi corazón, de hecho...")
            input("Jaja ntc, es solo una perla. No es una perla mágica ni nada, solo una muy bonita. Puedes benderla o hacerla joyería, para lo que me importa.\n")
            input("¿Decepcionante? Bueno, si te hace sentir mejor puedes verlo como una metáfora sobre cómo el verdadero tesoro son los amigos que hicimos en el camino o algo así\n")
            input("Bueno, {nombre}. El pacto está sellado. ¿Quieres ir por unas cervezas o algo? Escuché de una cosa llamada azulito que he querido probar.\n")
            ###Completar jejeje Este es el final
            #CGI
            input("**HORAS MÁS TARDE**")
            input("""YYJJJ?????77777!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!777777??77??JYY5
JJJ??????7777!!!!!!!!!!!~~~~~~~~~~~~^^^^^^^^~~~~~^^^^~~~^^~^^^~~~~^^^^~^^~~~~~~~~!!!!!!7777777??JJYY
J?????7777!!!!!!!!!~~~~~~~~~~~~^^^^^^^~!!!^^^^^^^^^^^^^^^^^^^^^^~~!!!777777!!~^^^~~~!!!!!!!77777?JJY
J????77777!!!!!!~~~~~~~^~~~^~^~?PP5!~JB###GYP5?^^^^^^^^^^^^^^!?J5PGB####&&&&#BGPJ7~^~~~!!!!!7777?JJY
J???777777!!!!~~~~~~~^^75GGGBB#&&&&&#&&&&&&&&@BP~^^^^^^^^^:~5GB&&&&&&&&&&&&&&&&&&#BY!^~~!!!!!!77??JJ
?7777777!!!!!~~~~~^^^7P&&&&&&&&&&&&&&&&&&&&&&&BG!^^^^^^^^^7GGB&&&&&&&&&&&&&&&&&&&&&&#J^^~~!!!!77??JJ
?7777777!!!~~~~^^JP55&&&&&&&&&&&&&&&&&&&&&&&#GY7^^^^^^^^^~5J5&&&&&&&&&&&&&&&&&&&&&&&&&P7~~~!!!!77??J
777!!!!!!!~~~~~^!#&&&&&&&&&&&&&&&&&&&&&&&&&&#J^:^^^^^^^^:?!J&&&&&&&&&&&&&&&&&&&&&&&&&&&&G7~~!!!!7???
77!!!!!!!~~~~^~!P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&P^:^^^^^^^:7?#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#!^~~!!!7??
7!!!!!!!~~~~~^^P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@B7^^^^^^^:Y&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&G7~~!!77??
7!!!!!!!~~~~^^7&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@J:^^^::~G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y!~~!77??
77!!!!!!~~~^7PG&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#~:::!5#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&57~~!7???
?77!!!!~~~~^?#@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#P7Y&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&?~~!!7???
?77!!!!~~~~^^!G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&5^~~!!7??J
?777!!!~~~~^^~G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@Y^~~!!7??J
?77!!!~~~^^^~~?G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y^~~!!77??
77!!!!~~~~^^~J!Y&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&P#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&G7^~~!!77??
?77!!!!~~~~^^^?G#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BPY!^~~~!!!7??
?77!!!!~~~~^^^!YG&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#7!~^^^~~~!!!77??
777!!!!~~~^^^^^^!JB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#55PB&@&&&&&&&&&&&&&&&&&&&&&&B?:^^^^^~~~~!!77??
?77!!!!~~~^^^^::^7B&&&&&&&&&&&&&&&&&&&&&&&&&&&#G5J?77~:::^!YB&&&&&&&&&&&&&&&&&&&&#~:^^^^^^~~~~!!!7??
77!!!!~~~^^^^:!5B&&&&&&&&&&&&&&&&&&&&&&&&&&#57~^:::::^^^^^::^P&&&&&&&&&&&&&&&&&&&#~^^^^^^^~~~~!!!7??
777!!!~~~^^^!P&@&&&&&&&&&&&&&&&&&&&&&&&&&&&7::^^^^^^^^^::::::?&&&&&&&&&&&&&&&&&&&&Y:^^^^^^~~~~!!77??
77!!!!~~~^^Y&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@P^^^^^^^^^:::^~!7??Y#&&&&&&&&&&&&&&&&&&&&7:^^^^~~~~!!!7???
7!!!!~~~~^^B&&&&&&&&&&&&&&&&&&&&&&&&&&&&BJ^:::::::::^75B#&&&&&&&&&&&&&&&&&&&&&&&&&&#!:^^^~~~~!!77?JJ
77!!!~~~^^7&&&&&&&&&&&&&&&&&&&&&&&&&&&#?^:^~7?JY5PPPB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#!^^^~~~~!!77??J
77!!!~~~^~B&&&#&&&&&&&&&&&&&&&&&&&&&&&#PYJG#&&@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#~^^~~~~!!77??J
7!!!!~~^^J@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@5^^^~~~!!!7??J
7!!!~~^^^^?&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#~^^^~~~!!77??
7!~7BBY^^~P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7^^^~~~!!!7??
7!!J#&@5~G@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#!^~~~~!!7??J
7!J@&&&&B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@G^^~~!!!7?JJ
7!!P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y~~!!77?JYY
7!!!B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y7?#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B~~!!77?JJY
?7!~J&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&5:P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#~~!!77??JJ
?7!7G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B~~~!!77?JJ
?77!P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@Y^~~~!!7???
?7!?&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&G~^~~!!!7???
?7!P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#!^~~~!!!7???
?77#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&?^^~~~!!!7??J
?7?&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y^^^~~!!!77??J
?7J&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y~~~~~~!!777?JJ
J7J&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&J^~~~~~!!!777?JJ
J?J&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B?^~~~~~~!!777??JY
???#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&5~^~~~!~!!!7????J55
??7B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B?~~!!!!7!!!!7?JJJY55
5J7G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&5!!77??????7777?JJJYY5""")
            #FIN
            input("""                _               °         ',:'/¯/`:,            .:':'`:·          ,:´'`;' ‘ 
     ,·~:-·´::/:`:;_.-~^*/'^;         /:/_/::::/';'        /:::::::/`·,      /::::/;‘  
    /::::::_:/::::::::::::/:::'i        /:'     '`:/::;‘      /:·*'`·:/:::::' , /·´'`;/::';' 
  /·~-·´     `:;_,:·-~^*'`^:;        ;         ';:';‘    ,'         `:;::::'`i    ';:::'; 
 'i                            i/        |         'i::i     ;            '`;:::'i    'i::::i 
  `·,                     ,.·´          ';        ;'::i     i               `;:';    'i:::i' 
     `;         ,-·~:^*'´/;            'i        'i::i'     i      ,          \|     '|:::i°
      ';        ;-· ~·-;/:/'             ;       'i::;'     |     ,'`,                i:;'' ‚
      ';       ,.,      ,'/               ';       i:/'      'i    'i:::i',             ';/'   
       ;      ';:/`'*'*´                   ';     ;/ °      'i     ;::/ \           ;/'     
       ';     ;/'                           ';   / °         \    'i/    '`·,      ,''       
        \    /                              `'´       °      '`~´         '`·–·'´'        
          `'´             '                   ‘                                 ‘           """)
            input("""                _               °         ',:'/¯/`:,            .:':'`:·          ,:´'`;' ‘ 
     ,·~:-·´::/:`:;_.-~^*/'^;         /:/_/::::/';'        /:::::::/`·,      /::::/;‘  
    /::::::_:/::::::::::::/:::'i        /:'     '`:/::;‘      /:·*'`·:/:::::' , /·´'`;/::';' 
  /·~-·´     `:;_,:·-~^*'`^:;        ;         ';:';‘    ,'         `:;::::'`i    ';:::'; 
 'i                            i/        |         'i::i     ;            '`;:::'i    'i::::i 
  `·,                     ,.·´          ';        ;'::i     i               `;:';    'i:::i' 
     `;         ,-·~:^*'´/;            'i        'i::i'     i      ,          \|     '|:::i°
      ';        ;-· ~·-;/:/'             ;       'i::;'     |     ,'`,                i:;'' ‚
      ';       ,.,      ,'/               ';       i:/'      'i    'i:::i',             ';/'   
       ;      ';:/`'*'*´                   ';     ;/ °      'i     ;::/ \           ;/'     
       ';     ;/'                           ';   / °         \    'i/    '`·,      ,''       
        \    /                              `'´       °      '`~´         '`·–·'´'        
          `'´             '                   ‘                                 ‘          """)
            input("""                _               °         ',:'/¯/`:,            .:':'`:·          ,:´'`;' ‘ 
     ,·~:-·´::/:`:;_.-~^*/'^;         /:/_/::::/';'        /:::::::/`·,      /::::/;‘  
    /::::::_:/::::::::::::/:::'i        /:'     '`:/::;‘      /:·*'`·:/:::::' , /·´'`;/::';' 
  /·~-·´     `:;_,:·-~^*'`^:;        ;         ';:';‘    ,'         `:;::::'`i    ';:::'; 
 'i                            i/        |         'i::i     ;            '`;:::'i    'i::::i 
  `·,                     ,.·´          ';        ;'::i     i               `;:';    'i:::i' 
     `;         ,-·~:^*'´/;            'i        'i::i'     i      ,          \|     '|:::i°
      ';        ;-· ~·-;/:/'             ;       'i::;'     |     ,'`,                i:;'' ‚
      ';       ,.,      ,'/               ';       i:/'      'i    'i:::i',             ';/'   
       ;      ';:/`'*'*´                   ';     ;/ °      'i     ;::/ \           ;/'     
       ';     ;/'                           ';   / °         \    'i/    '`·,      ,''       
        \    /                              `'´       °      '`~´         '`·–·'´'        
          `'´             '                   ‘                                 ‘          """)
            break
        elif shells < 2:
            input(f"La criatura posa su palma sobre tu pecho y te mira a los ojos. Sientes cómo te ruborizas y de pronto eres consciente del ritmo de tu respiración. Finalmente te dice: 'Oh, {nombre}, {nombre}, {nombre}. Volaste demasiado cerca del sol.', dice y luego te besa la frente. Sus labios te dejan una sensación viscosa en la piel que se va extendiendo al resto de  tu cuerpo. Vas notando cómo se expande hasta que te envuelve por completo, inovilizándote")
            input("'Felices 500 años, {nombre}. Espero que te guste este lugar tanto como a mí.', te dice {nereida} mientras se aleja de ti y se sumerge en el mar. Solo escuchas su risa en el eco oscuro de tu nuevo hogar")
            input("""  __                  _            
 /__  _. ._ _   _    / \     _  ._ 
 \_| (_| | | | (/_   \_/ \/ (/_ |  
                                   """)
            break
    elif game == "Trivia":
        input =f"{nereida} se relame los labios con una lengua puntiaguda y te dice 'Finalmente algo de emoción en todo esto. Bien, {nombre}, presta atención porque solo tienes una oportunidad'\n"
        acertijo = input(f"'Por los próximos 500 años de la libertad de tu alma inmortal, responde: ¿Cuál era el nombre del mar primordial, madre de todos nosotros?'\nO sea, puedes googlearlo, solo soy un script, ¿qué puedo hacer para detenerte?\n")
        if acertijo =="Talasa" or acertijo == "Thalassa" or acertijo =="Lady Gaga" or acertijo == "Mare":
            input(f"'Alguien ha estado leyendo sobre mitología en Wikipedia, ¿verdad? Pues ganaste, {nombre}'")
            input(f"'Lo que había originalmente adentro de la ostra era esto', dice mientras esculca entre sus branquias y saca una perla negra del tamaño de una pelota de golf.\n")
            #CGI Corazón
            input(""" BBGPP5YYJJYYY5Y55PGGBBBP5Y?Y&B##GB@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#GGPP55PBGPPPPPPGGPPPGGBBB##&&&&@
##BBGP55YJ?JJJJJY5PB#BPPP5J!J##&#P#@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@#P555PYYBG5PPPPPPP5555GB###&&&&@@@@
##BBBGPP5YJ?77???J5GBBGPYY?!^7#&&G5#@#B&@@@@@@@@@@@@@@@@@@@@@@@&PYYY55J?B#555555YJJ?JYGB&@@@@@@@@@@@
@&#BBBPPPP5?7!!777?JY5PGPY?!!~!B&#PP&&GB@@@@@@@@@@@@@@@@@@@@@@&5?JYY???YBGP55YJ???7?5G#&@@@@@@@@@@@@
@@@&&#B555P57!!!!!!!!!!?YYYJ?7!7G#5YB@BG#@@@@@@@@@@@@@@@@@@@@#YJJYJ77?JJ555555YJJ??5B&@@@@@@@@@@@@@@
@@@@@@&PY5PP?!~!!777!!!777?J?77!!5B5?PBB##@@@@@@@@@@@@@@@@@@BYJJ????777JY555YYJ?77?5B#&@@@@@@@@@@@@@
@@@@@@@&YJYPY!!7??7!!!7777?JYPP5YPB&P!7YGB#@@@@@@@@@@@@@@&GY??777?7~!7?JYYYY5PPGGBGPGB&@@@@@@@@@@@@@
@@@@@@@@B?J57~!7!~~~~~~~!!7??JPBGGB&&5!!7?J5B&@@@@@@@@@BJ!~~~~^!77!77777????JYY5PB&BYB@@@@@@@@@@@@@@
&&&&&&@@@Y?7~!!~~~^^~^^~!!7JYYPB#B#&@#57!7?JYG#&@@@@@G7^^^^^^:^7777!~~~~~!!77??JYYPBBG#@@@@@@@@@@@@@
@@&&&&@@@Y~!!!~~^^~^~~~7?JY55PG#&&&&&&#Y?JJJY5PB#@@@P^:::::^^:~??7!~^^^^~~~~!!77?JYYPBB#@@@@@@@@@@@@
&&&&&&@&J~!!~^^^^^~~!!?JY5PGGB#&&&&##&&B5YYYY55GB#PB7^^::::::^7JJ7!~^^^^^^^^~~~!77?JY5PG#&@@@@@@@@@@
&&&&@@B7~~~~~^^^~~!7?J5PPGBB#&&&&####&&&GPPP555PBBBB7^::::::^~75Y?!!~^^^^^^^^^^~!!!7?JY5PG#@@@@@@@@@
&&@&BJ~~~~~~!!~!77?JY5PGB###&&&######&&&#BGPP55PGBB#J^::^^~~~!755JJ?7!~~^^^::::^^^^~!7??JJ5PB&@@@@@@
@#5?~~~~~!77?YYJJY5PPGB##&&&###BBB##&@&&#BGPPPPPGBB&Y^^^^^~!!7J5GP55Y?77!~^^:::^::^^!77777??J5G&@@@@
P!!~^~7?J?JY5PGPPGGGB##&&&&#BBBBBB#&&&&&##BGPPPPGBB&Y^^^^^~!7?J5PBBGPYJJ?7!~!~~^^^^~?!7!!!~!?YPB&@@@
7!!~^7?YY5PGGB######&&&&###BBBBBB##&@&&&##BGPPPPGBB&Y~^^^^~!7?J5PGB#BP5YJJ????7!!!7J?7?!!~~7J5GB&@@@
7!~^!?YPGGBB#&&&@&&&&&&###BBBBBB##&&&&&&&#BGPPPGBBB&Y~^^^^~!7??J5PGB#BGP5YJJJJJJY55B5J??!!!?Y5PB#@@@
7~^~?Y5PGB#&&&&&@&&&&&####BBBBB##&&&&&&&&##BGPGBB##&P7~^^^~!77?JJYPPPB#BGP55YY5PB##&&GJJ7!!7?J5GB&@@
!~~!?YPB#&&&&&&&@@&######BBB###&&&@&&&&&&#BBBBBBGPPG57!~~~~~~!7?JJY55Y5PBBGGPP5PP5G#@BP5J!!!!?YPB&@@
~~!7?5G#BB&&&@@@@&#######B####&&&@&&&&&&&##G5?7!~!!7?JJYYJ?!~~!7?JJJYYJ?JP###BBBGGGB#&&PJ7!!~!?5PB&@
~~!7JYGBG#&&@@@@@&###########&&&@&&&&&&&&BJ!~~^^~~~!7?JY5PGGPY7!!7?JJJYYJ7?P#&#BGPPPGB#G!!!!~!?Y5PB&
!!7?JYG#&&&&@@&&BGGG#######&&&@@&&&&&&&&57!!~^::::^^~~!?JY5PGBBP7~!77?JYY5YJYB##BGPYY5GG!!!!~!?Y5PB&
~!7J5B#&&&&@@&&&&&&&&&&&&&&&@@&&&&&&&@&Y7!~^:.    .:^^~77?Y5PGB#&Y~!~~?JJJJY55B##BBBBGPP?!777!7J55G#
77777JYG#@@@@@&&&&&&&@@@@@@@@@@@@@@@@@P?7!^.        :^~7?JJ5PGBB#&Y!???!!!777?YPB#BGGGB#PJ??7!7JY5G#
YY?7!7?YPB&@@@@@&&&&&&&&&&&##&&&&&&&&#Y?7!~:..    .:~!!?YY5P5JPB#&B~!77!!!!~~~~~!7?J5PGY!~~~!?Y5PGB&
P5Y?!!!?YPB&@@&&&#BGGGBBBGGGGB#&&&###B5Y?77!!~~^^~!777?JYPGG?:7PBBB7~!!!~~~!!!~~~~~^~~~~^~!?YPGB#&&@
#BP5Y?!7?5G&@&##BBGGGG#&&BGPPB##&##BBB5YJ?J????77?JJJJY5PGGGJ^!!YG5YJJ??7!!7?7~~!!!~~!7~~7YPB##&@@@@
&&&#GY7~J5G#&&#BBGGGGB#&&#B5PB#&##BBBBGYJJYYYJJJJY55PPPP5YJP5Y7!YGPBGP5YJJJYY?!!!!~^~7~!YB&&&@@@@@@@
@@@&J!!7YG#&&@&#BBGBBB#&&&G5PB#&##BBGGBBP5YYYYY55P5J??!~^:^7JJY5PG#&&##BPYY55J7!7?777!!YB&&&&&@@@@@@
@@@@G7?YP#&&&@@&#BB####&&#GGB#&###BGGGB#&BP55YY55557^^^^^~!7?J5PB&@@@@&&BGGBPYYGP?7~77?PG#&&&&@@@@@@
@@@@@5YG#&&&@@&#GPPPGB&#BP5J?777???JYJJ5P5YY5PPY?7777?JJYYY55PB#@@B5YYJYY5PGPYJY77?JJ55GB#&&@@@@@@@@
@@@@@&B###&@@@@B5YJJYY?!~^^^^~~~!7J5GBY7!!!~~7Y55555PPPPPGGB#&@@B?^^~~7JPGB##BP5YYPB#&###&&@@@@@@@@@
@@&&&&B7?B@@@&57!~~~!~~!!7?Y5555PPG##&&B7~^~!!?YP#&&#BB##&@@@&#G~^~!!?YG#&&@@@@@&##&&&&&@@@@@@@@@@@@
GPPPPGP7?PB#BPJ??7777?JY5G#&&BB####&&&&#P5YYPPG###B?!!7??JPP?!~7JJY5G#&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@
YY555P5YYPGBBGGGPPGBBBB#&&#####&&&&&&###BB###&&#&&&B5JJY5Y~^^~7JGB#######&##&&&&&&&&&&&&&@@@@@@&&###
7777JY5B##&&&&&&&&&&&&&&&##&&&&&#######BB#####&&&&&&#####?!?YPB####&########&&&&&&&&&&@@@@@@&##BGGPP
J?7?JY5GB#&&&&&&&&&&&&##&&&&&&&#########&&&&&&####&####&&GPB###BB###&&&&&&&&&&&@@@@@@@@@@@&#BGGP5YYY
JYPPGGBBB#&&@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&#BBBBBB##&&@@&&@@&&########&&&&@@@@@@@@@@@@@@@&&#BBGPPYJJ?
?7?JYPBB#&@@@@@@@@@@@@@@&&&&&&&&&@@@@@@@@&&&&&#B###&&&@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@&&##BBGGPPYJ?7
7??JY5PPPGGB&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&##BBBBGGGGP5J!?
YJ!~!!!?YPBB##&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&####BBBBBBGGGPGGGGGG57~J
@@#GYJJ?777?YG#&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&###BBBBBGGGGGGGGGPGGGP5PP5555555PPGGGY!~Y
@@@@&#BP5YJ77!7?Y5GB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGP55YYYYYYYJJJJJJJJJYYYYYYYYY5555555PPPPY~!5
@@@@@@@&#BGP5YJ?7?Y5PGB##&&&@@@@@@@@@@@@@@@@@@@&&#BBGP55YJJ??777777????JJ????JJJYYY5P5PGPPPPGGP57^?G
B@@@@@@@@@&&#BGPYJYPGBB#B#BB##&&@@@@@@@@@@@@@&#BGPP5YYJ??777!!7777????JJJ?JJJYYYY5Y5GBBBBBBGGG5J~~YG
PBP#@@@@@@@@@@&#BPYYPGB###&&&&&&&&&&@@@@@@@&#BGP5YYJJ???7777777??????JJJJJJJJY55Y5YPB####BBBG5?!~?PB
##P#@&&@@@@@@@@@@&BP5PB###&&&@@&&&&&&&&&@@&#BBP55YYYYJJJJJJJJJJJJJJJYYYY55YYPPPBGGG##B###BBGPY?!~YGB """)
            input("Es mi corazón, de hecho...")
            input("Jaja ntc, es solo una perla. No es una perla mágica ni nada, solo una muy bonita. Puedes benderla o hacerla joyería, para lo que me importa.\n")
            input("¿Decepcionante? Bueno, si te hace sentir mejor puedes verlo como una metáfora sobre cómo el verdadero tesoro son los amigos que hicimos en el camino o algo así\n")
            input("Bueno, {nombre}. El pacto está sellado. ¿Quieres ir por unas cervezas o algo? Escuché de una cosa llamada azulito que he querido probar.\n")
            ###Completar jejeje Este es el final
            #CGI
            input("""YYJJJ?????77777!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!777777??77??JYY5
JJJ??????7777!!!!!!!!!!!~~~~~~~~~~~~^^^^^^^^~~~~~^^^^~~~^^~^^^~~~~^^^^~^^~~~~~~~~!!!!!!7777777??JJYY
J?????7777!!!!!!!!!~~~~~~~~~~~~^^^^^^^~!!!^^^^^^^^^^^^^^^^^^^^^^~~!!!777777!!~^^^~~~!!!!!!!77777?JJY
J????77777!!!!!!~~~~~~~^~~~^~^~?PP5!~JB###GYP5?^^^^^^^^^^^^^^!?J5PGB####&&&&#BGPJ7~^~~~!!!!!7777?JJY
J???777777!!!!~~~~~~~^^75GGGBB#&&&&&#&&&&&&&&@BP~^^^^^^^^^:~5GB&&&&&&&&&&&&&&&&&&#BY!^~~!!!!!!77??JJ
?7777777!!!!!~~~~~^^^7P&&&&&&&&&&&&&&&&&&&&&&&BG!^^^^^^^^^7GGB&&&&&&&&&&&&&&&&&&&&&&#J^^~~!!!!77??JJ
?7777777!!!~~~~^^JP55&&&&&&&&&&&&&&&&&&&&&&&#GY7^^^^^^^^^~5J5&&&&&&&&&&&&&&&&&&&&&&&&&P7~~~!!!!77??J
777!!!!!!!~~~~~^!#&&&&&&&&&&&&&&&&&&&&&&&&&&#J^:^^^^^^^^:?!J&&&&&&&&&&&&&&&&&&&&&&&&&&&&G7~~!!!!7???
77!!!!!!!~~~~^~!P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&P^:^^^^^^^:7?#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#!^~~!!!7??
7!!!!!!!~~~~~^^P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@B7^^^^^^^:Y&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&G7~~!!77??
7!!!!!!!~~~~^^7&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@J:^^^::~G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y!~~!77??
77!!!!!!~~~^7PG&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#~:::!5#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&57~~!7???
?77!!!!~~~~^?#@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#P7Y&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&?~~!!7???
?77!!!!~~~~^^!G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&5^~~!!7??J
?777!!!~~~~^^~G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@Y^~~!!7??J
?77!!!~~~^^^~~?G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y^~~!!77??
77!!!!~~~~^^~J!Y&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&P#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&G7^~~!!77??
?77!!!!~~~~^^^?G#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BPY!^~~~!!!7??
?77!!!!~~~~^^^!YG&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#7!~^^^~~~!!!77??
777!!!!~~~^^^^^^!JB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#55PB&@&&&&&&&&&&&&&&&&&&&&&&B?:^^^^^~~~~!!77??
?77!!!!~~~^^^^::^7B&&&&&&&&&&&&&&&&&&&&&&&&&&&#G5J?77~:::^!YB&&&&&&&&&&&&&&&&&&&&#~:^^^^^^~~~~!!!7??
77!!!!~~~^^^^:!5B&&&&&&&&&&&&&&&&&&&&&&&&&&#57~^:::::^^^^^::^P&&&&&&&&&&&&&&&&&&&#~^^^^^^^~~~~!!!7??
777!!!~~~^^^!P&@&&&&&&&&&&&&&&&&&&&&&&&&&&&7::^^^^^^^^^::::::?&&&&&&&&&&&&&&&&&&&&Y:^^^^^^~~~~!!77??
77!!!!~~~^^Y&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@P^^^^^^^^^:::^~!7??Y#&&&&&&&&&&&&&&&&&&&&7:^^^^~~~~!!!7???
7!!!!~~~~^^B&&&&&&&&&&&&&&&&&&&&&&&&&&&&BJ^:::::::::^75B#&&&&&&&&&&&&&&&&&&&&&&&&&&#!:^^^~~~~!!77?JJ
77!!!~~~^^7&&&&&&&&&&&&&&&&&&&&&&&&&&&#?^:^~7?JY5PPPB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#!^^^~~~~!!77??J
77!!!~~~^~B&&&#&&&&&&&&&&&&&&&&&&&&&&&#PYJG#&&@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#~^^~~~~!!77??J
7!!!!~~^^J@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@5^^^~~~!!!7??J
7!!!~~^^^^?&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#~^^^~~~!!77??
7!~7BBY^^~P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7^^^~~~!!!7??
7!!J#&@5~G@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#!^~~~~!!7??J
7!J@&&&&B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@G^^~~!!!7?JJ
7!!P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y~~!!77?JYY
7!!!B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y7?#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B~~!!77?JJY
?7!~J&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&5:P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#~~!!77??JJ
?7!7G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B~~~!!77?JJ
?77!P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@Y^~~~!!7???
?7!?&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&G~^~~!!!7???
?7!P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#!^~~~!!!7???
?77#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&?^^~~~!!!7??J
?7?&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y^^^~~!!!77??J
?7J&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Y~~~~~~!!777?JJ
J7J&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&J^~~~~~!!!777?JJ
J?J&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B?^~~~~~~!!777??JY
???#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&5~^~~~!~!!!7????J55
??7B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B?~~!!!!7!!!!7?JJJY55
5J7G&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&5!!77??????7777?JJJYY5""")
            #FIN
            input("""                _               °         ',:'/¯/`:,            .:':'`:·          ,:´'`;' ‘ 
     ,·~:-·´::/:`:;_.-~^*/'^;         /:/_/::::/';'        /:::::::/`·,      /::::/;‘  
    /::::::_:/::::::::::::/:::'i        /:'     '`:/::;‘      /:·*'`·:/:::::' , /·´'`;/::';' 
  /·~-·´     `:;_,:·-~^*'`^:;        ;         ';:';‘    ,'         `:;::::'`i    ';:::'; 
 'i                            i/        |         'i::i     ;            '`;:::'i    'i::::i 
  `·,                     ,.·´          ';        ;'::i     i               `;:';    'i:::i' 
     `;         ,-·~:^*'´/;            'i        'i::i'     i      ,          \|     '|:::i°
      ';        ;-· ~·-;/:/'             ;       'i::;'     |     ,'`,                i:;'' ‚
      ';       ,.,      ,'/               ';       i:/'      'i    'i:::i',             ';/'   
       ;      ';:/`'*'*´                   ';     ;/ °      'i     ;::/ \           ;/'     
       ';     ;/'                           ';   / °         \    'i/    '`·,      ,''       
        \    /                              `'´       °      '`~´         '`·–·'´'        
          `'´             '                   ‘                                 ‘           """)
            input("""                _               °         ',:'/¯/`:,            .:':'`:·          ,:´'`;' ‘ 
     ,·~:-·´::/:`:;_.-~^*/'^;         /:/_/::::/';'        /:::::::/`·,      /::::/;‘  
    /::::::_:/::::::::::::/:::'i        /:'     '`:/::;‘      /:·*'`·:/:::::' , /·´'`;/::';' 
  /·~-·´     `:;_,:·-~^*'`^:;        ;         ';:';‘    ,'         `:;::::'`i    ';:::'; 
 'i                            i/        |         'i::i     ;            '`;:::'i    'i::::i 
  `·,                     ,.·´          ';        ;'::i     i               `;:';    'i:::i' 
     `;         ,-·~:^*'´/;            'i        'i::i'     i      ,          \|     '|:::i°
      ';        ;-· ~·-;/:/'             ;       'i::;'     |     ,'`,                i:;'' ‚
      ';       ,.,      ,'/               ';       i:/'      'i    'i:::i',             ';/'   
       ;      ';:/`'*'*´                   ';     ;/ °      'i     ;::/ \           ;/'     
       ';     ;/'                           ';   / °         \    'i/    '`·,      ,''       
        \    /                              `'´       °      '`~´         '`·–·'´'        
          `'´             '                   ‘                                 ‘          """)
            input("""                _               °         ',:'/¯/`:,            .:':'`:·          ,:´'`;' ‘ 
     ,·~:-·´::/:`:;_.-~^*/'^;         /:/_/::::/';'        /:::::::/`·,      /::::/;‘  
    /::::::_:/::::::::::::/:::'i        /:'     '`:/::;‘      /:·*'`·:/:::::' , /·´'`;/::';' 
  /·~-·´     `:;_,:·-~^*'`^:;        ;         ';:';‘    ,'         `:;::::'`i    ';:::'; 
 'i                            i/        |         'i::i     ;            '`;:::'i    'i::::i 
  `·,                     ,.·´          ';        ;'::i     i               `;:';    'i:::i' 
     `;         ,-·~:^*'´/;            'i        'i::i'     i      ,          \|     '|:::i°
      ';        ;-· ~·-;/:/'             ;       'i::;'     |     ,'`,                i:;'' ‚
      ';       ,.,      ,'/               ';       i:/'      'i    'i:::i',             ';/'   
       ;      ';:/`'*'*´                   ';     ;/ °      'i     ;::/ \           ;/'     
       ';     ;/'                           ';   / °         \    'i/    '`·,      ,''       
        \    /                              `'´       °      '`~´         '`·–·'´'        
          `'´             '                   ‘                                 ‘          """)
            break
        else:
            input("'Oh, {nombre}, {nombre}, {nombre}. Volaste demasiado cerca del sol.', dice y luego te besa la frente. Sus labios te dejan una sensación viscosa en la piel que se va extendiendo al resto de  tu cuerpo. Vas notando cómo se expande hasta que te envuelve por completo, inovilizándote")
            input("'Felices 500 años, {nombre}. Espero que te guste este lugar tanto como a mí.', te dice {nereida} mientras se aleja de ti y se sumerge en el mar. Solo escuchas su risa en el eco oscuro de tu nuevo hogar")
            input("""  __                  _            
 /__  _. ._ _   _    / \     _  ._ 
 \_| (_| | | | (/_   \_/ \/ (/_ |  
                                   """)
    else:
            input("'Eso no es una opción, verga. Estamos hablando de tu plan de vida para los próximos 500 años, ¿seriedad es mucho pedir? ¿Magia o Trivia?'")
            continue