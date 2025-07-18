# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T15:01:47+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import (
    RdcerCertificatePostRequest,
    RdcerCertificatePostResponse,
    RdcerCertificatePostResponse1,
    RdcerCertificatePostResponse2,
    RdcerCertificatePostResponse3,
    RdcerCertificatePostResponse4,
    RdcerCertificatePostResponse5,
    RdcerCertificatePostResponse6,
    RegriiCertificatePostRequest,
    RegriiCertificatePostResponse,
    RegriiCertificatePostResponse1,
    RegriiCertificatePostResponse2,
    RegriiCertificatePostResponse3,
    RegriiCertificatePostResponse4,
    RegriiCertificatePostResponse5,
    RegriiCertificatePostResponse6,
    RmcerCertificatePostRequest,
    RmcerCertificatePostResponse,
    RmcerCertificatePostResponse1,
    RmcerCertificatePostResponse2,
    RmcerCertificatePostResponse3,
    RmcerCertificatePostResponse4,
    RmcerCertificatePostResponse5,
    RmcerCertificatePostResponse6,
)

app = MCPProxy(
    description="Department of Revenue, Registration & Land Reforms, Jharkhand (http://www.jharkhand.gov.in/revenue) is issuing Registration Certificate of Deeds into citizens' DigiLocker accounts from 5th May 2017 onwards.",
    termsOfService='https://apisetu.gov.in/terms.php',
    title='Revenue, Registration & Land Reforms Department, Jharkhand',
    version='3.0.0',
    servers=[{'url': 'https://apisetu.gov.in/enibandhanjh/v3'}],
)


@app.post(
    '/rdcer/certificate',
    description=""" API to verify Copy of Registered Deed. """,
    tags=['certificate_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def rdcer(body: RdcerCertificatePostRequest = None):
    """
    Copy of Registered Deed
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/regrii/certificate',
    description=""" API to verify ROR Register 2. """,
    tags=['certificate_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def regrii(body: RegriiCertificatePostRequest = None):
    """
    ROR Register 2
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/rmcer/certificate',
    description=""" API to verify Marriage Certificate. """,
    tags=['certificate_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def rmcer(body: RmcerCertificatePostRequest = None):
    """
    Marriage Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
