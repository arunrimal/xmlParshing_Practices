import gzip
import shutil

# f_in = open("C:\\Users\\Dell\\Desktop\\XML parsing\\venv_xml\\file.txt",'rb')
# f_out = gzip.open("C:\\Users\\Dell\\Desktop\\XML parsing\\venv_xml\\file.txt.gzip", 'w')
# f_out.writelines(f_in)
# f_out.close()
# f_in.close()


with open('file_01.txt', 'rb') as f_in, gzip.open('file_01.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)