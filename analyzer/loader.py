import pandas as pd
from datetime import datetime

def fetch_dataset(size=10) -> pd.DataFrame:
    data = [
        {
            "lot_number": "79478697-ЗЦП1",
            "announcement": "14976840-1 Кресла офисные для сотрудников",
            "description": "Кресло",
            "customer": "ТОО 'Лечебно-оздоровительный комплекс 'Балхаш'",
            "quantity": 5,
            "amount": 160000.00,
            "method": "Запрос ценовых предложений",
            "date": "2024-05-10"
        },
        {
            "lot_number": "73982489-ЗЦП1",
            "announcement": "14976840-1 Кресла офисные для сотрудников",
            "description": "Кресло",
            "customer": "ТОО 'Лечебно-оздоровительный комплекс 'Балхаш'",
            "quantity": 2,
            "amount": 90000.00,
            "method": "Запрос ценовых предложений",
            "date": "2024-05-12"
        },
        {
            "lot_number": "79478625-ЗЦП1",
            "announcement": "14976838-1 Вещевой тревожный чемодан для силовых структур",
            "description": "Рюкзак",
            "customer": "РГУ 'Департамент УИС по Атырауской области'",
            "quantity": 62,
            "amount": 2604000.00,
            "method": "Запрос ценовых предложений",
            "date": "2024-05-13"
        },
        {
            "lot_number": "79478789-ЗЦП1",
            "announcement": "14976837-1 Полотенца разных типов",
            "description": "Полотенце",
            "customer": "ТОО 'ЛОК 'Балхаш'",
            "quantity": 100,
            "amount": 330000.00,
            "method": "Запрос ценовых предложений",
            "date": "2024-05-15"
        },
        {
            "lot_number": "78435946-ОК3",
            "announcement": "14954185-1 Приобретение серверного оборудования",
            "description": "Сервер",
            "customer": "ГУ 'Аппарат акима Костанайской области'",
            "quantity": 2,
            "amount": 8839285.72,
            "method": "Открытый конкурс",
            "date": "2024-05-18"
        },
        {
            "lot_number": "79478641-ЗЦП1",
            "announcement": "14976824-1 Погоны-муфты специальные",
            "description": "Погоны",
            "customer": "РГУ 'Департамент УИС по Атырауской области'",
            "quantity": 70,
            "amount": 92400.00,
            "method": "Запрос ценовых предложений",
            "date": "2024-05-19"
        },
        {
            "lot_number": "79440292-ЗЦП2",
            "announcement": "14976811-1 Смесь строительная (шпаклевка гипсовая)",
            "description": "Смесь строительная",
            "customer": "ГУ 'Аппарат акима Коксуского с/о'",
            "quantity": 3,
            "amount": 10500.00,
            "method": "Запрос ценовых предложений",
            "date": "2024-05-20"
        }
    ]

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df.rename(columns={"amount": "price", "description": "item"}, inplace=True)
    df["supplier"] = "ТОО КазПоставка"  
    df["num_participants"] = [2, 1, 1, 1, 1, 1, 2]  
    return df

