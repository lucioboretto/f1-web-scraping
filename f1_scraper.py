from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def get_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    return driver


def scrape_f1_drivers(years):
    driver = get_driver()
    data_total = []

    for year in years:
        url = f"https://lat.motorsport.com/f1/drivers/?y={year}"
        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        pilotos = soup.find_all(
            "a",
            class_="ms-item--driver ms-item-vert-d ms-item-vert-t ms-item-vert-m"
        )

        for piloto in pilotos:
            nombre = piloto.find("p", class_="ms-item__title").text.strip()

            pais = None
            fecha = None
            equipo = None

            rows = piloto.find_all("div", class_="ms-item-driver__info-row")

            for row in rows:
                texto = row.get_text(strip=True)

                if "Nacionalidad" in texto:
                    pais = texto.replace("Nacionalidad:", "").strip()

                if "Fecha de nacimiento" in texto:
                    fecha = texto.replace(
                        "Fecha de nacimiento:", "").split("(")[0].strip()

                if "Equipo" in texto:
                    equipo = texto.replace("Equipo:", "").strip()

            data_total.append({
                "nombre": nombre,
                "pais": pais,
                "fecha_nacimiento": fecha,
                "equipo": equipo,
                "year": year
            })

    driver.quit()

    df = pd.DataFrame(data_total)
    return df


def clean_data(df):
    df = df.sort_values(by=["year", "nombre"])
    return df


def save_data(df, path="data/f1_drivers_dataset.csv"):
    df.to_csv(path, index=False)
    print(f"✅ Dataset guardado en {path}")


def main():
    years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

    df = scrape_f1_drivers(years)

    print(df.shape)
    print(df.head())

    print("Valores nulos:")
    print(df.isnull().sum())

    df = clean_data(df)

    save_data(df)


if __name__ == "__main__":
    main()
