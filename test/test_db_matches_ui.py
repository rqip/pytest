from model.group import Group
from timeit import timeit

def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=100))

    assert False
    #assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
    list1 = sorted(ui_list, key=Group.id_or_max)
    list2 = sorted(db_list, key=Group.id_or_max)
    #assert list1 == list2
