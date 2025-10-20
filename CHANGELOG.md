# Changelog

All notable changes to this project will be documented in this file.

## [v0.2] - 2025-10-20
### Added
- New trained model `model_v0.2.joblib` with improved prediction accuracy.
- Updated `train_model.py` script to save the new model.
- Updated API to load `model_v0.2` for predictions.

### Changed
- Refactored Dockerfile to include the new model and support future versions.
- Minor improvements in `app/main.py` for version handling and logging.

### Fixed
- Fixed bug where API would fail if the model file was missing.
- Updated dependencies in `requirements.txt` to latest stable versions.

## [v0.1] - 2025-10-19
### Added
- Initial version of FastAPI service with endpoints `/health` and `/predict`.
- Initial trained model `model_v0.1.joblib`.
- Docker support for v0.1 image.
