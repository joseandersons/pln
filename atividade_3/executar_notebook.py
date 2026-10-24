"""Executa a atividade inteira em um kernel novo do interpretador atual."""

import json
import sys
import tempfile
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from jupyter_client.kernelspec import KernelSpecManager


def main():
    pasta = Path(__file__).resolve().parent
    caminho = pasta / 'atividade_3_agrupamento_busca.ipynb'
    notebook = nbformat.read(caminho, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
            cell.metadata.pop('execution', None)

    inicio = time.monotonic()

    def salvar(**kwargs):
        nbformat.write(notebook, caminho)

    def progresso(cell, cell_index, **kwargs):
        if cell.cell_type == 'code':
            print(f'[{time.monotonic() - inicio:.0f}s] Executando célula {cell_index + 1}/{len(notebook.cells)}', flush=True)

    # O kernelspec temporário evita depender de um kernel global ou de outro venv.
    pasta_temporaria = pasta / '.python-deps'
    pasta_temporaria.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='kernel-', dir=pasta_temporaria) as temp:
        kernels = Path(temp)
        spec = kernels / 'atividade3'
        spec.mkdir()
        (spec / 'kernel.json').write_text(json.dumps({
            'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
            'display_name': 'Atividade 3 (validação)',
            'language': 'python',
            'env': {'PYTHONIOENCODING': 'utf-8', 'MPLBACKEND': 'module://matplotlib_inline.backend_inline'},
        }), encoding='utf-8')
        cliente = NotebookClient(
            notebook, timeout=3600, kernel_name='atividade3',
            resources={'metadata': {'path': str(pasta)}},
            on_cell_start=progresso, on_cell_executed=salvar,
        )
        km = cliente.create_kernel_manager()
        km.kernel_spec_manager = KernelSpecManager(kernel_dirs=[str(kernels)])
        cliente.km = km
        km.connection_file = str(kernels / 'connection.json')
        try:
            cliente.execute()
        finally:
            salvar()
            if cliente.km is not None:
                cliente._cleanup_kernel()
    print(f'Concluído em {time.monotonic() - inicio:.0f}s: {caminho.name}', flush=True)


if __name__ == '__main__':
    main()
