from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 



# Data validation artifact ke liye code hai jo congif_entity ke badd add krna hai 
# Ab component/data_validation me jao aur vala code add kro 
@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str
    validation_report_file_path: str




# # Ye file path return karega like niche diy gye files name ka path return karega
# #  Ab component/data_transformation file me jao aur code add karo

# @dataclass
# class DataTransformationArtifact:
#     transformed_object_file_path:str 
#     transformed_train_file_path:str
#     transformed_test_file_path:str


# # Model trainer ke liy hai jo Classification metric return karega aur trained model file ka path return karega
# # Ab component/model_trainer file me jao aur code add kro

# @dataclass
# class ClassificationMetricArtifact:
#     f1_score:float
#     precision_score:float
#     recall_score:float



# @dataclass
# class ModelTrainerArtifact:
#     trained_model_file_path:str 
#     metric_artifact:ClassificationMetricArtifact



# # Model S3 bucket me push krne ke bad
# # Eske bad component/model_evaluation me code add krna hai 
# @dataclass
# class ModelEvaluationArtifact:
#     is_model_accepted:bool
#     changed_accuracy:float
#     s3_model_path:str 
#     trained_model_path:str


# # Model pusher ke liy code hai jo model evalation ke bad add hoga (agar model evaluation me model acccept hota hai to hi !)
# # Ab Component/model_pusher me jao aur code add kro
# @dataclass
# class ModelPusherArtifact:
#     bucket_name:str
#     s3_model_path:str    