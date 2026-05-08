import time



asciiart = r"""     
   _        ___       _     _ _                        
  / \      / _ \ _ __| |__ (_) |_ _   _               
  | |     | | | | '__| '_ \| | __| | | |              
 /|_|\    | |_| | |  | |_) | | |_| |_| |              
///|\\\    \___/|_|  |_.__/|_|\__|\__, |             
                                  |___/   

         O R B I T Y - v1.0.1        
"""

header = r"""
Author: M.R.L Silva;
Project: Orbity - A rockertics simulation software for educational purposes;
Institution: Instituto Federal de Educação, Ciência e Tecnologia de Alagoas - IFAL-PIN;
Advisor: Prof. Dr. Karciano José Silva Santos;
"""

options1 = r"""
[01] - More about the project
[02] - View Important Notices
[03] - Intrusions Manual
[04] - Start the program
[00] - Exit
"""

print(f"\033[38;5;208m{asciiart}\033[0m")
print(f"\033[38;2;64;224;208m{header}\033[0m")
print(f"\033[38;2;64;224;208m{options1}\033[0m")

pergunta = input('\033[38;2;64;224;208mPlease select an option: \033[0m').strip()

