# F1 Drivers Web Scraping

## Español

Este script extrae información de pilotos de Fórmula 1 desde la web de Motorsport para distintos años y genera un dataset en formato CSV.

### Librerías necesarias

```bash
pip install pandas
pip install selenium
pip install beautifulsoup4
```

### Ejecución

```bash
python src/f1_scraper.py
```

### Funcionamiento

El script:

* Accede dinámicamente a la web de Motorsport
* Extrae información de pilotos para múltiples temporadas
* Procesa y limpia los datos
* Guarda los resultados en un archivo CSV

### Datos extraídos

Actualmente se extrae la siguiente información de cada piloto:

* Nombre (`nombre`)
* Nacionalidad (`pais`)
* Fecha de nacimiento (`fecha_nacimiento`)
* Equipo (`equipo`)
* Año (`year`)

### Output

Los datos se almacenan en:

```bash
data/f1_drivers_dataset.csv
```

## English

This script extracts Formula 1 drivers data from the Motorsport website for multiple seasons and generates a structured CSV dataset.

### Required libraries

```bash
pip install pandas
pip install selenium
pip install beautifulsoup4
```

### Run the script

```bash
python src/f1_scraper.py
```

### How it works

The script:

* Dynamically accesses the Motorsport website
* Extracts drivers data across multiple seasons
* Cleans and processes the data
* Saves the results into a CSV file

### Extracted data

The dataset includes:

* Driver name (`nombre`)
* Nationality (`pais`)
* Birth date (`fecha_nacimiento`)
* Team (`equipo`)
* Season year (`year`)

### Output

The data is stored in:

```bash
data/f1_drivers_dataset.csv
```
