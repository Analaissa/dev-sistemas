from app.database import SessionLocal
from app.models import Departamento, Cargo

def popular_banco():
    db = SessionLocal()  # abrir sessão
    try:
        # Se já tem dados, não inserir de novo
        if db.query(Departamento).count() > 0:
            print('Banco já preenchido. Pulando...')
            return

        db.add_all([
            Departamento(nome='Tecnologica da Informação', silga='TI'),
            Departamento(nome='Recurso Humano', sigla='RH'),
            Departamento(nome='Finaceiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM'),
        ])

        db.add_all([
            Cargo(titulo='Desenvolvedor', nivel='Junior', salario_min=2500, salario_max=4000),
            Cargo(tiutlo='desenvolvedor', nivel='pleno', salario_min=4000, salario_max=7000),
            Cargo(titulo='designer', nivel='Junior', salario_min=2200, salario_max=3500),
            Cargo(titulo='Analistar RH', nivel='pleno', salario_min=3500, salario_max=6000),
        ])
        db.commit()  # confirma tudo no banco de uma vez
        print('Banco preenchindo com sucesso')
    except Exception as erro:
        db.rollback()  # desfaz tudo se de erro
        print(f'Erro: {erro}')
    finally:
         db.close()   # lembre-se sempre de fechar a sessão
if __name__=='__main__':
    popular_banco()