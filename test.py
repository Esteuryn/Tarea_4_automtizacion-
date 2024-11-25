import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración global del navegador
@pytest.fixture
def browser():
    browser = webdriver.Chrome()  # Asegúrate de tener el chromedriver configurado
    base_url = "http://127.0.0.1:5501/index.html"  # Cambia la ruta según tu sistema de archivos
    browser.get(base_url)
    yield browser
    browser.quit()

# Función para pausar la ejecución
def espera(tiempo):
    time.sleep(tiempo)

# Historia de Usuario 1: Navegar a Paella Valenciana y regresar
def test_historia1(browser):
    enlace = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Paella Valenciana"))
    )
    enlace.click()
    espera(3)
    assert "paella.html" in browser.current_url, "No se abrió la página correcta de Paella Valenciana"
    browser.save_screenshot("captura_historia1_paella.png")
    volver = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".volver")))
    volver.click()
    assert "index.html" in browser.current_url, "No se volvió a la página principal"

# Historia de Usuario 2: Navegar a Gazpacho Andaluz y regresar
def test_historia2(browser):
    enlace = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Gazpacho Andaluz"))
    )
    enlace.click()
    espera(3)
    assert "gazpacho.html" in browser.current_url, "No se abrió la página correcta de Gazpacho Andaluz"
    browser.save_screenshot("captura_historia2_gazpacho.png")
    volver = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".volver")))
    volver.click()
    assert "index.html" in browser.current_url, "No se volvió a la página principal"

# Historia de Usuario 3: Navegar a Fabada Asturiana y regresar
def test_historia3(browser):
    enlace = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Fabada Asturiana"))
    )
    enlace.click()
    espera(3)
    assert "fabada.html" in browser.current_url, "No se abrió la página correcta de Fabada Asturiana"
    browser.save_screenshot("captura_historia3_fabada.png")
    volver = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".volver")))
    volver.click()
    assert "index.html" in browser.current_url, "No se volvió a la página principal"

# Historia de Usuario 4: Navegar a Tortilla Española y regresar
def test_historia4(browser):
    enlace = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Tortilla Española"))
    )
    enlace.click()
    espera(3)
    assert "tortilla.html" in browser.current_url, "No se abrió la página correcta de Tortilla Española"
    browser.save_screenshot("captura_historia4_tortilla.png")
    volver = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".volver")))
    volver.click()
    assert "index.html" in browser.current_url, "No se volvió a la página principal"

# Historia de Usuario 5: Navegar a Crema Catalana y regresar
def test_historia5(browser):
    enlace = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Crema Catalana"))
    )
    enlace.click()
    espera(3)
    assert "crema-catalana.html" in browser.current_url, "No se abrió la página correcta de Crema Catalana"
    browser.save_screenshot("captura_historia5_crema_catalana.png")
    volver = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".volver")))
    volver.click()
    assert "index.html" in browser.current_url, "No se volvió a la página principal"