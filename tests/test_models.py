from app.models.planet import Planet
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mars",
                    description="where aliens live",
                    color="red")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] == "where aliens live"
    assert result["color"] == "red"

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Mars",
                    description="where aliens live",
                    color="red")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mars"
    assert result["description"] == "where aliens live"
    assert result["color"] == "red"

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                    description="where aliens live",
                    color="red")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "where aliens live"

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mars",
                    color="red")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] is None
    assert result["color"] == "red"

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "New Planet",
        "description": "The Best Planet!",
        "color": "pink"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best Planet!"
    assert new_planet.color == "pink"

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "The Best Planet!",
        "color": "pink"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "New planet",
        "color": "pink"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "New Planet",
        "description": "The Best Planet!",
        "color": "pink",
        "another": "last value"
    }
    
    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best Planet!"
