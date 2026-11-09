from app.database import engine, SessionLocal, Base
from app import models
from app.crud import inserir_tutor, inserir_animal, inserir_atendimento

# Cria todas as tabelas (na ordem correta — SQLAlchemy resolve as FKs)
Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()

    try:
        # Tutores
        t1 = inserir_tutor(db, "Ana", "(61) 99999-1111", "ana@email.com")
        t2 = inserir_tutor(db, "Carlos", "(61) 99999-2222", "carlos@email.com")
        t3 = inserir_tutor(db, "Marcela", "(61) 99999-3333", "marcela@email.com")

        print(f"Tutores cadastrados: {t1.nome_completo}, {t2.nome_completo}, {t3.nome_completo}")

        # Animais
        a1 = inserir_animal(db, "Fofinho", "Cachorro", "PitBull", 32.5, t1.id)
        a2 = inserir_animal(db, "Garfield", "Gato", "Persa", 4.2, t2.id)
        a3 = inserir_animal(db, "Lila","Cachorro", "Pincher", 8.0, t1.id)
        a4 = inserir_animal(db, "Marley", "Gato", "Siamês", 3.8, t3.id)
        a5 = inserir_animal(db, "Mel", "Cachorro", "Labrador", 28.0, t2.id)

        print(f"Animais cadastrados: {a1.nome_animal}, {a2.nome_animal}, {a3.nome_animal}, "
              f"{a4.nome_animal}, {a5.nome_animal}")

        # Atendimentos
        at1 = inserir_atendimento(db, "31/07/2025", "Consulta de rotina", 150.00, a1.id)
        at2 = inserir_atendimento(db, "02/10/2025", "Vacina antirrábica", 80.00, a2.id)
        at3 = inserir_atendimento(db, "13/08/2025", "Banho e tosa", 60.00, a3.id)
        at4 = inserir_atendimento(db, "04/01/2025", "Exame de sangue", 120.00, a4.id)
        at5 = inserir_atendimento(db, "25/02/2025", "Castração", 350.00, a5.id)
        at6 = inserir_atendimento(db, "06/04/2025", "Retorno pós-cirúrgico", 80.00, a5.id)
        at7 = inserir_atendimento(db, "17/06/2025", "Consulta — problema de pele", 150.00, a1.id)

        print(f"Atendimentos registrados: {at1.id}, {at2.id}, {at3.id}, "
              f"{at4.id}, {at5.id}, {at6.id}, {at7.id}")

        print("\nBanco criado. Arquivo: clinica_vetpet.db")

    finally:
        db.close()


if __name__ == "__main__":
    main()