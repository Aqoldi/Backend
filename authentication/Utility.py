from drf_yasg.inspectors import SwaggerAutoSchema


class CustomSchema(SwaggerAutoSchema):
    def get_operation(self, operation_keys):
        operation = super().get_operation(operation_keys)
        Valid_Urls = [
            "POST /auth/users/",
            "GET /auth/users/{UserId}/",
            "PATCH /auth/users/{UserId}/",
            "DELETE /auth/users/{UserId}/"
        ]
        # print(f"{self.method} {self.path}" )
        print(operation)
        if "jwt" in self.path or f"{self.method} {self.path}" in Valid_Urls:
            return operation
        return None
