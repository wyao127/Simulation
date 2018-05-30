import argparse

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Parse original file name.')
   parser.add_argument('-f', dest="file_name", default="", type=str, help="source file")      
   parser.add_argument('-p', dest="pattern", default=None, type=str, help="pattern string")       
   parser.add_argument('-w', dest="waveform", default=0, type=int, help="enable waveform generating")
   parser.add_argument('-m', dest="mix", default=1, type=int, help="mix with normal traffic")            

   args = parser.parse_args()
   
   file_name = args.file_name
