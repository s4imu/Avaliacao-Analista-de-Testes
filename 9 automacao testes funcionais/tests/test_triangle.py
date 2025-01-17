import pytest
from pages.triangle_page import TrianglePage

@pytest.mark.parametrize(
    "setup_teardown, vertice1, vertice2, vertice3, expected_result",
    [
        ("https://www.vanilton.net/triangulo/#", 3, 3, 3, "Equilátero"),
        ("https://www.vanilton.net/triangulo/#", 4, 4, 3, "Isósceles"),
        ("https://www.vanilton.net/triangulo/#", 5, 4, 3, "Escaleno"),
        ("https://www.vanilton.net/triangulo/#", 10, 2, 2, "Os lados informados não formam um triângulo"),
        ("https://www.vanilton.net/triangulo/#", 0, 0, 0, "Valores inválidos"),
        ("https://www.vanilton.net/triangulo/#", -1, -1, -1, "Valores inválidos"),
        ("https://www.vanilton.net/triangulo/#", "a", "b", "c", "Valores inválidos"),
    ],
    indirect=["setup_teardown"],
)
@pytest.mark.usefixtures("setup_teardown")
class TestTriangulo:
    def test_ct01_which_triangle(self, vertice1, vertice2, vertice3, expected_result):
        # Arrange
        triangle_page = TrianglePage()

        # Act
        triangle_page.fill_vertices(vertice1, vertice2, vertice3)
        triangle_page.click_indetify_button()

        # Assert
        obtained_result = triangle_page.get_result()
        assert expected_result in obtained_result, f"Expected: {expected_result}, Obtained: {obtained_result}"
