class get:
    def help():
        print(
            """
     Penda Version - v2.67
     Penda is Official Programming language created by Krish Anjara 

     Format: penda [OPTIONS] | [COMMANDS] 
     Manual Page : 'man penda'
     Usage: penda [ -h | --help] [ -V | --version ] [ -f | --file ] < FILE > [ -U | --update ]
                  [ --uninstall ] 

     [OPTIONS]
     Short  |   Long        Description...

     -f     |   --file      Requires a file written in penda script
                            To execute.
     -S     |   --shell     Opens Interactive shell of Penda script
                            to use 
     -V     |   --version   Prints the version of program
     -U     |   --update    Updates to the latest version Of Penda
     -h     |   --help      Prints this help message

     [COMMANDS]
     
     uninstall   =>    Will uninstall Penda from your device
                       Use 'uninstall-full' to delete the Installer
     config      =>    To edit enviroment variable and to edit 
                       setting functions
     help        =>    Use help to get more information of command
                       ex. "penda help config"

     To reinstall penda Type "penda-install" in terminal
     
      """
        )

    def version():
        print(
            """
             Penda Version: v2.67
             Penda is Official Programming language created by Krish Anjara
             """
        )
