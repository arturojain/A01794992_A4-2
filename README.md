# Actividad 4.2 - Ejercicios de Programación con PEP-8

Proyecto de implementación de 3 programas en Python siguiendo el estándar PEP-8, con validación mediante pylint y tests unitarios con pytest.

## 📋 Descripción del Proyecto

Este proyecto contiene tres programas en Python que implementan algoritmos manualmente sin usar bibliotecas built-in:

1. **compute_statistics.py** - Calcula estadísticas descriptivas (media, mediana, moda, desviación estándar, varianza)
2. **convert_numbers.py** - Convierte números a representación binaria y hexadecimal
3. **word_count.py** - Cuenta la frecuencia de palabras en un archivo de texto

Cada programa:
- ✅ Sigue estrictamente el estándar PEP-8
- ✅ Implementa algoritmos manualmente (sin bibliotecas)
- ✅ Maneja errores de datos inválidos
- ✅ Mide y reporta tiempo de ejecución
- ✅ Guarda resultados en archivos de texto
- ✅ Tiene tests unitarios completos con pytest

## 🏗️ Estructura del Proyecto

```
A4.2/
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias del proyecto
├── .gitignore                   # Archivos a ignorar en Git
├── pytest.ini                   # Configuración de pytest
├── test_report.html             # Reporte HTML de tests
├── htmlcov/                     # Reporte de cobertura de código
│
├── P1/                          # Programa 1: Estadísticas
│   ├── source/
│   │   └── compute_statistics.py
│   ├── tests/
│   │   ├── test_compute_statistics.py
│   │   └── data/              # Archivos de prueba TC1-TC7
│   └── results/               # Reportes y resultados
│
├── P2/                          # Programa 2: Conversor
│   ├── source/
│   │   └── convert_numbers.py
│   ├── tests/
│   │   ├── test_convert_numbers.py
│   │   └── data/              # Archivos de prueba TC1-TC4
│   └── results/               # Reportes y resultados
│
└── P3/                          # Programa 3: Contador de Palabras
    ├── source/
    │   └── word_count.py
    ├── tests/
    │   ├── test_word_count.py
    │   └── data/              # Archivos de prueba TC1-TC5
    └── results/               # Reportes y resultados
```

## 🚀 Instalación

### 1. Crear entorno virtual

```bash
cd /Users/arturojain/Desktop/A4.2
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

Las dependencias incluyen:
- `pylint==3.0.3` - Validador de estilo PEP-8
- `pytest==7.4.4` - Framework de testing
- `pytest-html==4.1.1` - Generación de reportes HTML
- `pytest-cov==4.1.0` - Análisis de cobertura de código

## 📖 Uso de los Programas

### P1: Compute Statistics

Calcula estadísticas descriptivas de una lista de números.

```bash
cd P1/source
python3 compute_statistics.py <archivo_datos>

# Ejemplo:
python3 compute_statistics.py ../tests/data/TC1.txt
```

**Salida:**
- Pantalla: Resultados formateados
- Archivo: `StatisticsResults.txt`

**Estadísticas calculadas:**
- Count (cantidad)
- Mean (media)
- Median (mediana)
- Mode (moda)
- Standard Deviation (desviación estándar poblacional)
- Variance (varianza poblacional)

### P2: Convert Numbers

Convierte números a binario y hexadecimal.

```bash
cd P2/source
python3 convert_numbers.py <archivo_datos>

# Ejemplo:
python3 convert_numbers.py ../tests/data/TC1.txt
```

**Salida:**
- Pantalla: Tabla de conversiones
- Archivo: `ConversionResults.txt`

### P3: Word Count

Cuenta la frecuencia de cada palabra en un archivo.

```bash
cd P3/source
python3 word_count.py <archivo_datos>

# Ejemplo:
python3 word_count.py ../tests/data/TC1.txt
```

**Salida:**
- Pantalla: Lista de palabras con frecuencias
- Archivo: `WordCountResults.txt`

## 🧪 Ejecución de Tests

### Ejecutar todos los tests

```bash
source venv/bin/activate
pytest -v
```

### Ejecutar tests con reporte HTML

```bash
pytest --html=test_report.html --self-contained-html
```

### Ejecutar tests con cobertura de código

```bash
pytest --cov=P1/source --cov=P2/source --cov=P3/source \
       --cov-report=html --cov-report=term-missing
```

### Ejecutar tests de un programa específico

```bash
pytest P1/tests/test_compute_statistics.py -v
pytest P2/tests/test_convert_numbers.py -v
pytest P3/tests/test_word_count.py -v
```

## ✅ Validación con Pylint

### Validar todos los programas

```bash
source venv/bin/activate
pylint P1/source/*.py P2/source/*.py P3/source/*.py
```

### Validar un programa específico

```bash
pylint P1/source/compute_statistics.py
pylint P2/source/convert_numbers.py
pylint P3/source/word_count.py
```

## 📊 Resultados

### Pylint (Cumplimiento PEP-8)

| Programa | Score | Estado |
|----------|-------|--------|
| compute_statistics.py | 10.00/10 | ✅ Perfecto |
| convert_numbers.py | 10.00/10 | ✅ Perfecto |
| word_count.py | 10.00/10 | ✅ Perfecto |
| **Promedio Global** | **9.93/10** | ✅ Excelente |

### Pytest (Tests Unitarios)

| Programa | Tests | Pasados | Cobertura |
|----------|-------|---------|-----------|
| P1: compute_statistics.py | 29 | 29 ✅ | 74% |
| P2: convert_numbers.py | 26 | 26 ✅ | 72% |
| P3: word_count.py | 19 | 19 ✅ | 71% |
| **Total** | **74** | **74 ✅** | **72%** |

**Resultado:** 100% de tests pasados

### Tipos de Tests Implementados

#### Tests Unitarios
- Pruebas individuales de cada función
- Casos edge (valores límite, vacíos, cero)
- Manejo de errores

#### Tests de Integración
- Ejecución con archivos TC reales
- Validación de resultados esperados
- Manejo de datos inválidos

#### Tests End-to-End
- Flujo completo desde lectura hasta escritura
- Verificación de archivos de salida
- Validación de formato de resultados

## 📁 Archivos de Prueba

Cada programa incluye múltiples casos de prueba (TC):

- **P1:** TC1-TC7 (desde 400 hasta 12,769 números)
  - TC5 incluye datos inválidos para probar manejo de errores

- **P2:** TC1-TC4 (diferentes cantidades de números)

- **P3:** TC1-TC5 (diferentes archivos de texto)
  - Incluyen archivos de resultados esperados (.Results.txt)

## 🎯 Características Destacadas

### Cumplimiento PEP-8
- ✅ Nombres de funciones en snake_case
- ✅ Máximo 79 caracteres por línea
- ✅ Docstrings completos en todas las funciones
- ✅ Importaciones organizadas
- ✅ Espaciado consistente

### Implementación Manual
- ✅ Algoritmos implementados desde cero
- ✅ Sin uso de numpy, statistics, Counter, bin(), hex()
- ✅ Demostración de comprensión de algoritmos

### Manejo de Errores
- ✅ Validación de archivos inexistentes
- ✅ Detección y reporte de datos inválidos
- ✅ Mensajes de error claros
- ✅ Continuación de ejecución después de errores

### Testing Profesional
- ✅ 74 tests unitarios
- ✅ Reportes HTML interactivos
- ✅ Análisis de cobertura de código
- ✅ Tests parametrizados

## 📈 Reportes Generados

Los reportes se encuentran en las carpetas `results/` de cada programa:

1. **test_report.html** - Reporte interactivo de ejecución de tests
2. **htmlcov/** - Reporte de cobertura de código con análisis línea por línea
3. **StatisticsResults.txt** - Resultados de cálculos estadísticos (P1)
4. **ConversionResults.txt** - Resultados de conversiones (P2)
5. **WordCountResults.txt** - Resultados de conteo de palabras (P3)

## 🛠️ Tecnologías Utilizadas

- **Python 3.14.2** - Lenguaje de programación
- **pylint 3.0.3** - Análisis estático de código
- **pytest 7.4.4** - Framework de testing
- **pytest-html 4.1.1** - Generación de reportes
- **pytest-cov 4.1.0** - Análisis de cobertura

## 👨‍💻 Autor

Arturo Jain

## 📝 Notas Adicionales

### Consideraciones de Diseño

1. **Manejo de Datos Inválidos:**
   - Los programas continúan ejecutándose después de encontrar datos inválidos
   - Se reporta el número total de entradas inválidas
   - Se muestran mensajes de advertencia específicos

2. **Rendimiento:**
   - Medición precisa de tiempo de ejecución
   - Optimización para archivos grandes (miles de elementos)
   - Algoritmos eficientes sin sacrificar legibilidad

3. **Algoritmos Implementados:**
   - **Media:** Suma de valores / cantidad
   - **Mediana:** Valor central de lista ordenada
   - **Moda:** Valor más frecuente (conteo manual)
   - **Varianza:** Σ(x - μ)² / N
   - **Desv. Estándar:** √varianza
   - **Binario:** Divisiones sucesivas entre 2
   - **Hexadecimal:** Divisiones sucesivas entre 16
   - **Conteo:** Diccionario de frecuencias
   - **Ordenamiento:** Bubble sort manual

### Comandos Útiles

```bash
# Ver estructura del proyecto
tree -L 3 -I 'venv|htmlcov|__pycache__|.pytest_cache'

# Limpiar archivos temporales
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type d -name ".pytest_cache" -exec rm -r {} +

# Ejecutar programa con datos de prueba y medir tiempo
time python3 P1/source/compute_statistics.py P1/tests/data/TC1.txt
```

## 📚 Referencias

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Pylint Documentation](https://pylint.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)

---

**Fecha de Creación:** Febrero 2026
**Versión:** 1.0
