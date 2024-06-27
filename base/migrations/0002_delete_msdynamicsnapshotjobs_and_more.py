# Generated by Django 5.0.6 on 2024-06-25 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Msdynamicsnapshotjobs',
        ),
        migrations.DeleteModel(
            name='Msdynamicsnapshotviews',
        ),
        migrations.DeleteModel(
            name='MsmergeAgentParameters',
        ),
        migrations.DeleteModel(
            name='MsmergeAltsyncpartners',
        ),
        migrations.DeleteModel(
            name='MsmergeArticlehistory',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictsInfo',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1Baithi',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1Bode',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1Coso',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1CtBaithi',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1Giaovien',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1GiaovienDangky',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1Khoa',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1Lop',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1Monhoc',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs1Sinhvien',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2Baithi',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2Bode',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2Coso',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2CtBaithi',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2Giaovien',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2GiaovienDangky',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2Khoa',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2Lop',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2Monhoc',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnCs2Sinhvien',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnTcLop',
        ),
        migrations.DeleteModel(
            name='MsmergeConflictTtnTcSinhvien',
        ),
        migrations.DeleteModel(
            name='MsmergeContents',
        ),
        migrations.DeleteModel(
            name='MsmergeCurrentPartitionMappings',
        ),
        migrations.RemoveField(
            model_name='msmergedynamicsnapshots',
            name='partition',
        ),
        migrations.DeleteModel(
            name='MsmergeErrorlineage',
        ),
        migrations.DeleteModel(
            name='MsmergeGenerationPartitionMappings',
        ),
        migrations.DeleteModel(
            name='MsmergeGenhistory',
        ),
        migrations.DeleteModel(
            name='MsmergeHistory',
        ),
        migrations.DeleteModel(
            name='MsmergeIdentityRange',
        ),
        migrations.DeleteModel(
            name='MsmergeLogFiles',
        ),
        migrations.DeleteModel(
            name='MsmergeMetadataactionRequest',
        ),
        migrations.DeleteModel(
            name='MsmergePastPartitionMappings',
        ),
        migrations.DeleteModel(
            name='MsmergeReplinfo',
        ),
        migrations.DeleteModel(
            name='MsmergeSessions',
        ),
        migrations.DeleteModel(
            name='MsmergeSettingshistory',
        ),
        migrations.DeleteModel(
            name='MsmergeSupportabilitySettings',
        ),
        migrations.DeleteModel(
            name='MsmergeTombstone',
        ),
        migrations.DeleteModel(
            name='MsreplErrors',
        ),
        migrations.DeleteModel(
            name='Sysdiagrams',
        ),
        migrations.DeleteModel(
            name='Sysmergearticles',
        ),
        migrations.DeleteModel(
            name='Sysmergepartitioninfo',
        ),
        migrations.DeleteModel(
            name='Sysmergepublications',
        ),
        migrations.DeleteModel(
            name='Sysmergeschemaarticles',
        ),
        migrations.DeleteModel(
            name='Sysmergeschemachange',
        ),
        migrations.DeleteModel(
            name='Sysmergesubscriptions',
        ),
        migrations.DeleteModel(
            name='Sysmergesubsetfilters',
        ),
        migrations.DeleteModel(
            name='Sysreplservers',
        ),
        migrations.DeleteModel(
            name='MsmergeDynamicSnapshots',
        ),
        migrations.DeleteModel(
            name='MsmergePartitionGroups',
        ),
    ]
