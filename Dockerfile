FROM public.ecr.aws/lambda/python:3.9
RUN python -m pip install --upgrade pip
RUN pip install fastapi[all] uvicorn mangum pandas xarray[complete] numpy h5netcdf netCDF4 fsspec boto3 s3fs zarr rio-tiler[complete] rioxarray
ADD . .
RUN pip install -e .
ENV HOST="0.0.0.0"
ENV PORT=8000
ENTRYPOINT uvicorn server:app --host ${HOST} --port ${PORT}
