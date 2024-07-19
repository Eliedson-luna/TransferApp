import shutil
import datetime
import os
import traceback
from configparser import ConfigParser


# acesso do arquivo config

cfg = ConfigParser()
cfg.read("Assets/config.cfg")
cfg.sections()
src_path = cfg['general']["src_path"]
dst_path = cfg["general"]["dst_path"]
transfer_path = cfg["general"]["transf_path"]

archives_src = os.listdir(src_path)
archives_transfer = os.listdir(transfer_path)

# area de funções

def chkPath():
    global transfer_area
    if not os.path.isdir(transfer_path):
        transfer_area = os.mkdir(transfer_path)
    else: 
        transfer_area = transfer_path

def transfer(arch):
    with open("log.txt", "a", encoding="utf-8")as log:
        if os.path.isdir(src_path+arch):
            log.write("\n-")
            log.write(f"\n{arch} is a directory")
            try:
                log.write(f"\nCopiando arquivo {arch} para a area de tranferencia")
                shutil.copytree(f"S:/WorkSpaces/{arch}", f"{transfer_area}{arch}")
            except Exception as e:
                log.write("\nNao foi possivel copiar para a pasta de tranferencia\n")
                log.write(f"ERRO: {e} --> {traceback.format_exc()}")
            try:
                log.write(f"\nRemovendo arquivo {arch} da pasta de destino {dst_path}")
                shutil.rmtree(f"{dst_path}{arch}")
            except Exception as e:
                log.write("\nNao foi possivel remover o arquivo da pasta de destino")
                log.write(f"ERRO: {e} --> {traceback.format_exc()}")
            try:
                log.write("\nMovendo o arquivo de pasta de transferencia para a pasta de destino")
                shutil.move(f"{transfer_area}{arch}", f"{dst_path}{arch}")
            except Exception as e:
                log.write(f"\nnao foi possivel mover {arch}")
                log.write(f"ERRO: {e} --> {traceback.format_exc()}")

def clearTransferPath(arch):
    with open("log.txt", "a", encoding="utf-8")as log:
        try:
            log.write("\nEsvaziando pasta de transferencia")
            shutil.rmtree(f"{transfer_area}{arch}")
        except Exception as e:
            log.write(f"\nNao foi possivel excluir {arch}")
            log.write(f"ERRO: {e} --> {traceback.format_exc()}")

def initInfo():
    with open("log.txt", "a", encoding="utf-8")as log:
        log.write(f"\n\nINICIANDO ARCHIVE TRANSFER\n\nData: {data()}\n")
        log.write(f"\nPastas: {archives_src}\n")
    
def data():
    data = datetime.datetime.now()
    dataformatada = f"{data.day}/{data.month}/{data.year} Hr: {data.hour}:{data.minute}"
    return dataformatada

def exec():
    chkPath()
    with open("log.txt", "a", encoding="utf-8")as log:
        initInfo()
        try:
            if os.path.isdir(dst_path):
                for arch in archives_transfer:
                    clearTransferPath(arch)
                for arch in archives_src:
                    transfer(arch)
            else:
                raise Exception(f"A pasta {dst_path} não está disponivel")   
        except Exception as e:
            log.write(f"\nERRO --> {e}")
            
        log.write("\n-")
        log.write("\nTarefa Completa\n"+("-"*50)) 



