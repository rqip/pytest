# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    #assert len(old_groups) + 1 == app.group.count()    #after commit=True
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
