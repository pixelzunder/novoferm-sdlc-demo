from doorcfg.models import DoorConfiguration, opening_area_cm2


def test_opening_area_in_square_centimetres(base_config: DoorConfiguration) -> None:
    # 2500 mm x 2125 mm = 250 cm x 212.5 cm
    assert opening_area_cm2(base_config) == 53_125
