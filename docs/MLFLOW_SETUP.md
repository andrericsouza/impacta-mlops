# Guia: Instalar e executar MLflow localmente

Este guia mostra como configurar o MLflow para uso local em um laboratório, arquitetura básica e como navegar na UI.

Requisitos
- Python 3.8+ (recomendado 3.10)
- pip
- (Opcional) Conda

Instalação rápida (venv)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1    # PowerShell
pip install --upgrade pip
pip install mlflow sqlalchemy alembic
```

Executando localmente (modo simples)
- UI rápida (para uso local e desenvolvimento):
```powershell
mlflow ui --port 5000
# Abra http://127.0.0.1:5000
```

Executando um Tracking Server local (modo com persistência)
- Backend store: onde ficam metadados (SQLite, Postgres). Para laboratório, usamos SQLite:
```powershell
set BACKEND_URI=sqlite:///mlflow.db
set ARTIFACT_ROOT=./mlruns
mlflow server --backend-store-uri %BACKEND_URI% --default-artifact-root %ARTIFACT_ROOT% --host 0.0.0.0 --port 5000
```
- A UI ficará disponível em `http://localhost:5000`.

Arquitetura básica do MLflow
- Tracking Server: endpoint HTTP que recebe logs de runs.
- Backend Store: banco relacional contendo metadados (params, metrics, run info). Pode ser `sqlite`, `postgres`, `mysql`.
- Artifact Store: onde artefatos (modelos, plots, arquivos) são salvos (local FS, S3, GCS).
- Model Registry: API/DB para registrar e versionar modelos, promover para `Staging`/`Production`.

Como registrar experimentos a partir de notebooks
Exemplo mínimo usando a API do MLflow (Python):
```python
import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("diamond_experiment")
with mlflow.start_run():
    mlflow.log_param("model", "xgboost")
    mlflow.log_metric("rmse", 0.123)
    mlflow.log_artifact("path/to/plot.png")
```

Navegando na UI
- Experiments: lista de experiments; cada experiment contém runs.
- Runs: cada execução contém `params`, `metrics`, `artifacts` e `tags`.
- Compare Runs: selecione várias runs e compare parâmetros e métricas.
- Artifacts: baixe modelos, plots e arquivos salvos por run.
- Model Registry (se habilitado): gerencie versões de modelos, estágios e descrições.

Boas práticas para o laboratório
- Para simplicidade local, use `sqlite` + `./mlruns` como `artifact_root`.
- Não use SQLite em produção — prefira Postgres/MySQL para concorrência.
- Versione código e dados; armazene artefatos grandes em S3 ou similar.
- Use tags para identificar runs (e.g., `git_commit`, `dataset_version`, `user`).

Solução de problemas comuns
- Problema: UI não inicia na porta 5000 -> verificar se porta ocupada.
- Problema: não vê artifacts -> verificar `default-artifact-root` e permissões.

Referências rápidas
- MLflow docs: https://mlflow.org

