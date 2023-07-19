from chonker import chonkify


def test_chonkify():
    size = 10
    datalen = 100
    for rawindex, (chonk, _) in enumerate(chonkify(range(datalen), size=size)):
        assert chonk.size == size
        assert chonk.rawindex == rawindex
        assert chonk.index == rawindex // size
        assert chonk.subindex == rawindex % size
        assert chonk.is_start_of == (rawindex % size == 0)
        assert chonk.is_end_of == (rawindex % size == size - 1)
