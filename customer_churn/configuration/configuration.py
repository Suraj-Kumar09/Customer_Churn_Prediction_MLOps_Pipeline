from customer_churn.entity.config_entity import DataValidationConfig


def get_data_validation_config(self) -> DataValidationConfig:
    data_validation_dir = os.path.join(self.training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    
    data_validation_config = DataValidationConfig(
        data_validation_dir=data_validation_dir,
        drift_report_file_path=os.path.join(data_validation_dir, DATA_VALIDATION_DRIFT_REPORT_DIR, DATA_VALIDATION_DRIFT_REPORT_FILE_NAME),
        validation_report_file_path=os.path.join(data_validation_dir, "report.yaml") 
    )
    return data_validation_config