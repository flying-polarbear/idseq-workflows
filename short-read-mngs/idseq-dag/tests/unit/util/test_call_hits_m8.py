import unittest
import tempfile
import os
import shelve
import random
import dbm

from idseq_dag.util.m8 import call_hits_m8

from tests.unit.unittest_helpers import file_contents, relative_file_path

class TestLog(unittest.TestCase):
    def test_call_hits_m8(self):
        # This tests the logic based on a small sample. For development and performance benchmarking you can use real m8 outputs
        #   as well as the real taxid-lineages.db and accession2taxid.db (from s3://idseq-public-references/taxonomy or s3://idseq-public-references/alignment_data).

        # Generated by taking a random sample from a gsnap output on benchmark sample 5
        #   The random output took a cluster of five rows as it's smallest unit to make a more
        #   realistic file as similar rows are clustured.
        input_m8 = relative_file_path(__file__, 'm8-test/sample.m8')

        lineages = relative_file_path(__file__, 'm8-test/taxid-lineages.db')
        accession2taxid = relative_file_path(__file__, 'm8-test/accession2taxid.db')

        lineages_db = shelve.open(lineages.replace('.db', ''), 'c')
        accession2taxid_db = shelve.open(accession2taxid.replace('.db', ''), 'c')

        # Generated by running this test the full versions of these dicts and printing which items were needed
        accession2taxid_db["MK468611"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK468612"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK468613"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK468615"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK468617"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MH124576"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MH124577"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MH124578"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MH124579"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MH124580"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK286896"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK370031"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK370032"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK370033"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK468608"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["CP015500"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["CP015822"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["CP015990"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["CP016813"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["CP016814"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["CP018140"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["CP018337"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["CP018352"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["CP018356"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["CP018364"] = "573"
        lineages_db["573"] = ('573', '570', '543')
        accession2taxid_db["MK468618"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK468619"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK468620"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK468621"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MK468622"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MF740874"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MF773566"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MF774614"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MF774615"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["MF774616"] = "37124"
        lineages_db["37124"] = ('37124', '11019', '11018')
        accession2taxid_db["CP010295"] = "1280"
        lineages_db["1280"] = ('1280', '1279', '90964')
        accession2taxid_db["CP010296"] = "1280"
        lineages_db["1280"] = ('1280', '1279', '90964')
        accession2taxid_db["CP010297"] = "1280"
        lineages_db["1280"] = ('1280', '1279', '90964')
        accession2taxid_db["CP010298"] = "1280"
        lineages_db["1280"] = ('1280', '1279', '90964')
        accession2taxid_db["CP010299"] = "1280"
        lineages_db["1280"] = ('1280', '1279', '90964')
        accession2taxid_db["NC_038358"] = "2065052"
        lineages_db["2065052"] = ('2065052', '687333', '687329')
        accession2taxid_db["CP017682"] = "1280"
        lineages_db["1280"] = ('1280', '1279', '90964')
        accession2taxid_db["CP017804"] = "1280"
        lineages_db["1280"] = ('1280', '1279', '90964')
        accession2taxid_db["AF325855"] = "1280"
        lineages_db["1280"] = ('1280', '1279', '90964')
        accession2taxid_db["AM990992"] = "523796"
        lineages_db["523796"] = ('1280', '1279', '90964')
        accession2taxid_db["AP014652"] = "46170"
        lineages_db["46170"] = ('1280', '1279', '90964')

        lineages_db.close()
        accession2taxid_db.close()

        output_m8 = relative_file_path(__file__, 'm8-test/test.m8')
        output_summary = relative_file_path(__file__, 'm8-test/test.hitsummary.tab')

        call_hits_m8(
            input_m8,
            lineages,
            accession2taxid,
            output_m8,
            output_summary,
            36,
        )

        in_size = os.stat(input_m8).st_size
        out_size = os.stat(output_m8).st_size

        # File should shrink due to deduping
        self.assertLessEqual(out_size, in_size)

        # Generated by running this test then manually inspected
        sample_deduped_m8 = relative_file_path(__file__, 'm8-test/sample.deduped.m8')
        sample_summary = relative_file_path(__file__, 'm8-test/sample.hitsummary.tab')
        
        self.assertEqual(file_contents(output_m8), file_contents(sample_deduped_m8))
        self.assertEqual(file_contents(output_summary), file_contents(sample_summary))

        os.remove(output_m8)
        os.remove(output_summary)
        os.remove(lineages)
        os.remove(accession2taxid)
