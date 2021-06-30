import logic
from waitress import serve

host_name = '0.0.0.0'
port_num = 5200 
run = True
while(run):
    print(host_name,":",port_num," is statred")
    serve(logic.app,host=host_name,port=port_num)
    


    