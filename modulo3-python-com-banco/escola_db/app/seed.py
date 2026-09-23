from app.database import SessionLocal
from app.models import Curso, Aluno

def popular_banco():
  db =SessionLocal()
  try:
    if db.query(Curso).count()> 0:
      print('Banco já populado.pulando...')
      return

# inserir cursos
    db.add_all([
      Curso(nome='Desenvolvimento de Sistemas', duracao=1200),
      Curso(nome='informatica para Internet', duracao=1000),
      Curso(nome='Redes de computadores', duracao=800)
    ])
#inserir alunos
    db.add_all([      
      Curso(nome='Lucas Mendes', email='lucas@senai.com', matricula='2025001'),
      Curso(nome='Fernada Reis', email='fernada@senai.com',matricula='1283395'),
      Curso(nome='Rafael Souza', email='rafael@senai.com',matricula='2563981'),
      Curso(nome='Vitoria Silva',email='vitoria@senai.com',matricula='5236984'),
    ])
    db.commit()# confirmar no banco
    print('banco populado com sucesso!')
  except Exception as e:
    db.rollback() # desfazer se der erro
    print(f'Error:{e}')
  finally:
    db.close()
