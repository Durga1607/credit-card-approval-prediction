# IBM Deployment

This project is designed to support IBM Watson Machine Learning deployment.

During project development, IBM Cloud required account activation and billing verification before Watson Machine Learning services could be created.

As SmartBridge did not provide IBM Cloud activation credentials or a registration code, IBM deployment could not be completed during the submission period.

The application is fully functional using the trained Random Forest model integrated with the Flask web application.

Required IBM environment variables (to be configured later):

```
WATSON_API_KEY=
WATSON_URL=https://us-south.ml.cloud.ibm.com
WATSON_DEPLOYMENT_ID=
WATSON_SPACE_ID=
WATSON_MODEL_ID=
```

Once valid IBM Cloud credentials are available, the project can be deployed without changing the user interface.