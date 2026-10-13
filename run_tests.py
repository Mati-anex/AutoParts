
import subprocess
import sys


def ejecutar(comando, descripcion):
    print("\n" + "=" * 60)
    print(descripcion)
    print("=" * 60)

    resultado = subprocess.run(comando, check=False)

    if resultado.returncode != 0:
        print(f"\nEl comando terminó con errores: {descripcion}")
        return False

    print(f"\nFinalizado correctamente: {descripcion}")
    return True


def main():
    print("EVALUACION: PRUEBAS UNITARIAS Y COBERTURA")

    pruebas_ok = ejecutar(
        [sys.executable, "manage.py", "test"],
        "1. EJECUCION DE PRUEBAS UNITARIAS"
    )

    cobertura_ok = ejecutar(
        [
            sys.executable, "-m", "coverage",
            "run", "--source=.", "manage.py", "test"
        ],
        "2. EJECUCION DE PRUEBAS CON COBERTURA"
    )

    if cobertura_ok:
        ejecutar(
            [sys.executable, "-m", "coverage", "report", "-m"],
            "3. RESUMEN DE COBERTURA Y LINEAS NO CUBIERTAS"
        )

        ejecutar(
            [sys.executable, "-m", "coverage", "html"],
            "4. GENERACION DEL INFORME HTML"
        )

    if not pruebas_ok or not cobertura_ok:
        print("\nRESULTADO: revisar las pruebas y los errores anteriores.")
        sys.exit(1)

    print("\nRESULTADO: comandos de pruebas finalizados correctamente.")
    print("Revisa el resumen de cobertura y las lineas no cubiertas.")


if __name__ == "__main__":
    main()
