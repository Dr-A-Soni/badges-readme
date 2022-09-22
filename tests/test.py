#!/usr/bin/python3
# coding=UTF-8
import unittest, json
from unittest import TestCase
from unittest.mock import MagicMock, patch

from services.credly import Credly
from main import generate_new_readme

BASE_FOLDER="/badges/tests/"
FOLDER_MARKDOWNS=BASE_FOLDER+"markdowns/"
FOLDER_HTML=BASE_FOLDER+"html/"


def return_markdown(filename):
    with open(FOLDER_MARKDOWNS + filename, "r") as fh:
        return fh.read()


class Tests(TestCase):
    def test_canary(self):
        self.assertTrue(True)

class TestBadgeSize(TestCase):
    def setUp(self):
        self.maxDiff = None

        self.mocks = {}
        self.patches = []

        badge_size_patch = patch('services.credly.BADGE_SIZE', new='200')
        self.mocks['badge_size'] = badge_size_patch.start()
        self.patches.append(badge_size_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_happy_day(self):
        data = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        self.assertEqual(
            '[![ PYTHON FOR DATA SCIECNCE AND AI](https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png)](https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" PYTHON FOR DATA SCIECNCE AND AI")\n[![Predictive Modeling and Text Mining](https://images.credly.com/size/680x680/images/e98b…4112/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/ba4ac412-79a2-4d49-9c0f-b0a1548dae23"Predictive Modeling and Text Mining")\n[![Statistical Thinking and Problem Solving](https://images.credly.com/size/680x680/images/7b88…dc50/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/8995bdd4-eee7-4160-99b2-28683fb1782c"Statistical Thinking and Problem Solving")\n[![Correlation and Regression](https://images.credly.com/size/680x680/images/ad66…dcd4/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/a333254f-9448-4485-9a3e-08691ad06ea7"Correlation and Regression")\n[![Design of Experiments](https://images.credly.com/size/680x680/images/d96b…a128/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/3afac32d-3299-4337-80a3-a4150471c32b"Design of Experiments")\n[![Decision Making with Data](	https://images.credly.com/size/680x680/images/d05f…4575/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/eb253681-509f-4216-acbc-ee22db52b8b6"Decision Making with Data")\n[![Exploratory Data Analysis](	https://images.credly.com/size/680x680/images/60f3…e798/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/891f1247-1bfb-425a-af60-63837667cfbe"Exploratory Data Analysis")\n[![Quality Methods](https://images.credly.com/size/680x680/images/26b9…9096/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/f384bd74-1202-4b8c-aa7d-74f0937c815a"Quality Methods")\n[![Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression](https://images.credly.com/size/680x680/images/fe43…6_badges_EducationTraining_Learn_AdvAnalytics.png)](https://www.credly.com/earner/earned/badge/5b0712d7-f0e4-4cd9-9ace-830097efaff2"Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression")\n[![SAS Programming 1: Essentials](https://images.credly.com/size/680x680/images/c5d4…56_badges_EducationTraining_Learn_Programming.png)](https://www.credly.com/earner/earned/badge/0135e701-6c8b-484f-8a4b-81003ce99b31"SAS Programming 1: Essentials")',
            data,
        )

class TestNumberLastBadges(TestCase):
    def setUp(self):
        self.maxDiff = None

        self.mocks = {}
        self.patches = []

        badge_size_patch = patch('services.credly.NUMBER_LAST_BADGES', new=1)
        self.mocks['badge_size'] = badge_size_patch.start()
        self.patches.append(badge_size_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_happy_day(self):
        data = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        self.assertEqual(
            '[![ PYTHON FOR DATA SCIECNCE AND AI](https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png)](https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" PYTHON FOR DATA SCIECNCE AND AI")',
            data,
        )
class TestsCredly(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_happy_day(self):
        data = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        self.assertEqual(
            '[![ PYTHON FOR DATA SCIECNCE AND AI](https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png)](https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" PYTHON FOR DATA SCIECNCE AND AI")\n[![Predictive Modeling and Text Mining](https://images.credly.com/size/680x680/images/e98b…4112/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/ba4ac412-79a2-4d49-9c0f-b0a1548dae23"Predictive Modeling and Text Mining")\n[![Statistical Thinking and Problem Solving](https://images.credly.com/size/680x680/images/7b88…dc50/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/8995bdd4-eee7-4160-99b2-28683fb1782c"Statistical Thinking and Problem Solving")\n[![Correlation and Regression](https://images.credly.com/size/680x680/images/ad66…dcd4/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/a333254f-9448-4485-9a3e-08691ad06ea7"Correlation and Regression")\n[![Design of Experiments](https://images.credly.com/size/680x680/images/d96b…a128/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/3afac32d-3299-4337-80a3-a4150471c32b"Design of Experiments")\n[![Decision Making with Data](	https://images.credly.com/size/680x680/images/d05f…4575/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/eb253681-509f-4216-acbc-ee22db52b8b6"Decision Making with Data")\n[![Exploratory Data Analysis](	https://images.credly.com/size/680x680/images/60f3…e798/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/891f1247-1bfb-425a-af60-63837667cfbe"Exploratory Data Analysis")\n[![Quality Methods](https://images.credly.com/size/680x680/images/26b9…9096/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/f384bd74-1202-4b8c-aa7d-74f0937c815a"Quality Methods")\n[![Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression](https://images.credly.com/size/680x680/images/fe43…6_badges_EducationTraining_Learn_AdvAnalytics.png)](https://www.credly.com/earner/earned/badge/5b0712d7-f0e4-4cd9-9ace-830097efaff2"Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression")\n[![SAS Programming 1: Essentials](https://images.credly.com/size/680x680/images/c5d4…56_badges_EducationTraining_Learn_Programming.png)](https://www.credly.com/earner/earned/badge/0135e701-6c8b-484f-8a4b-81003ce99b31"SAS Programming 1: Essentials")',
            data,
        )

class testsHappyDayHTML(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_not_tag(self):
        no_tags = return_markdown("no_tags.md")
        self.assertEqual("# badge-readme\nThis is example file", no_tags)

        badges = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        new_readme = generate_new_readme(badges, no_tags)
        self.assertEqual("# badge-readme\nThis is example file", new_readme)

        self.assertEqual(no_tags, new_readme)

    def test_with_tags_no_text_between(self):
        with_tags_no_text_between = return_markdown("with_tags_no_text_between.md")
        self.assertEqual(
            "# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<!--END_SECTION:badges-->",
            with_tags_no_text_between,
        )

        badges = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        new_readme = generate_new_readme(badges, with_tags_no_text_between)
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n\n[![ PYTHON FOR DATA SCIECNCE AND AI](https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png)](https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" PYTHON FOR DATA SCIECNCE AND AI")\n[![Predictive Modeling and Text Mining](https://images.credly.com/size/680x680/images/e98b…4112/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/ba4ac412-79a2-4d49-9c0f-b0a1548dae23"Predictive Modeling and Text Mining")\n[![Statistical Thinking and Problem Solving](https://images.credly.com/size/680x680/images/7b88…dc50/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/8995bdd4-eee7-4160-99b2-28683fb1782c"Statistical Thinking and Problem Solving")\n[![Correlation and Regression](https://images.credly.com/size/680x680/images/ad66…dcd4/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/a333254f-9448-4485-9a3e-08691ad06ea7"Correlation and Regression")\n[![Design of Experiments](https://images.credly.com/size/680x680/images/d96b…a128/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/3afac32d-3299-4337-80a3-a4150471c32b"Design of Experiments")\n[![Decision Making with Data](	https://images.credly.com/size/680x680/images/d05f…4575/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/eb253681-509f-4216-acbc-ee22db52b8b6"Decision Making with Data")\n[![Exploratory Data Analysis](	https://images.credly.com/size/680x680/images/60f3…e798/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/891f1247-1bfb-425a-af60-63837667cfbe"Exploratory Data Analysis")\n[![Quality Methods](https://images.credly.com/size/680x680/images/26b9…9096/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/f384bd74-1202-4b8c-aa7d-74f0937c815a"Quality Methods")\n[![Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression](https://images.credly.com/size/680x680/images/fe43…6_badges_EducationTraining_Learn_AdvAnalytics.png)](https://www.credly.com/earner/earned/badge/5b0712d7-f0e4-4cd9-9ace-830097efaff2"Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression")\n[![SAS Programming 1: Essentials](https://images.credly.com/size/680x680/images/c5d4…56_badges_EducationTraining_Learn_Programming.png)](https://www.credly.com/earner/earned/badge/0135e701-6c8b-484f-8a4b-81003ce99b31"SAS Programming 1: Essentials")\n<!--END_SECTION:badges-->',
            new_readme,
        )

        self.assertNotEqual(with_tags_no_text_between, new_readme)

    def test_with_tags_text_between(self):
        with_tags_text_between = return_markdown("with_tags_text_between.md")
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<p align="left"><a href=" https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" title=" PYTHON FOR DATA SCIECNCE AND AI "><img src=" https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png " alt=" PYTHON FOR DATA SCIECNCE AND AI "></img></a><a href=" https://www.credly.com/earner/earned/badge/ba4ac412-79a2-4d49-9c0f-b0a1548dae23" title=" Predictive Modeling and Text Mining "><img src=" https://images.credly.com/size/680x680/images/e98b…4112/62056_badges_EducationTraining_Learn_JMP.png " alt="Predictive Modeling and Text Mining"></img></a><a href="https://www.credly.com/earner/earned/badge/8995bdd4-eee7-4160-99b2-28683fb1782c " title=" Statistical Thinking and Problem Solving "><img src=" https://images.credly.com/size/680x680/images/7b88…dc50/62056_badges_EducationTraining_Learn_JMP.png " alt=" Statistical Thinking and Problem Solving "></img></a> <a href=" https://www.credly.com/earner/earned/badge/a333254f-9448-4485-9a3e-08691ad06ea7" title=" Correlation and Regression "><img src=" https://images.credly.com/size/680x680/images/ad66…dcd4/62056_badges_EducationTraining_Learn_JMP.png " alt=" Correlation and Regression "></img></a><a href=" https://www.credly.com/earner/earned/badge/3afac32d-3299-4337-80a3-a4150471c32b " title=" Design of Experiments "><img src=" https://images.credly.com/size/680x680/images/d96b…a128/62056_badges_EducationTraining_Learn_JMP.png " alt=" Design of Experiments "></img></a><a href=" https://www.credly.com/earner/earned/badge/eb253681-509f-4216-acbc-ee22db52b8b6" title=" Decision Making with Data "><img src=" https://images.credly.com/size/680x680/images/d05f…4575/62056_badges_EducationTraining_Learn_JMP.png " alt=" Decision Making with Data "></img></a> <a href=" https://www.credly.com/earner/earned/badge/891f1247-1bfb-425a-af60-63837667cfbe " title=" Exploratory Data Analysis "><img src=" https://images.credly.com/size/680x680/images/60f3…e798/62056_badges_EducationTraining_Learn_JMP.png) " alt=" Exploratory Data Analysis "></img></a><a href=" https://www.credly.com/earner/earned/badge/f384bd74-1202-4b8c-aa7d-74f0937c815a " title=" Quality Methods "><img src=" https://images.credly.com/size/680x680/images/26b9…9096/62056_badges_EducationTraining_Learn_JMP.png " alt=" Quality Methods "></img></a><a href=" https://www.credly.com/earner/earned/badge/5b0712d7-f0e4-4cd9-9ace-830097efaff2" title=" Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression "><img src="https://images.credly.com/size/680x680/images/fe43…6_badges_EducationTraining_Learn_AdvAnalytics.png " alt=" Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression "></img></a><a href="https://www.credly.com/earner/earned/badge/0135e701-6c8b-484f-8a4b-81003ce99b31" title=" SAS Programming 1: Essentials "><img src=" https://images.credly.com/size/680x680/images/c5d4…56_badges_EducationTraining_Learn_Programming.png " alt=" SAS Programming 1: Essentials "></img></a></p> \n<!--END_SECTION:badges-->',
            with_tags_text_between,
        )

        badges = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        new_readme = generate_new_readme(badges, with_tags_text_between)
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n\n[![ PYTHON FOR DATA SCIECNCE AND AI](https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png)](https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" PYTHON FOR DATA SCIECNCE AND AI")\n[![Predictive Modeling and Text Mining](https://images.credly.com/size/680x680/images/e98b…4112/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/ba4ac412-79a2-4d49-9c0f-b0a1548dae23"Predictive Modeling and Text Mining")\n[![Statistical Thinking and Problem Solving](https://images.credly.com/size/680x680/images/7b88…dc50/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/8995bdd4-eee7-4160-99b2-28683fb1782c"Statistical Thinking and Problem Solving")\n[![Correlation and Regression](https://images.credly.com/size/680x680/images/ad66…dcd4/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/a333254f-9448-4485-9a3e-08691ad06ea7"Correlation and Regression")\n[![Design of Experiments](https://images.credly.com/size/680x680/images/d96b…a128/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/3afac32d-3299-4337-80a3-a4150471c32b"Design of Experiments")\n[![Decision Making with Data](	https://images.credly.com/size/680x680/images/d05f…4575/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/eb253681-509f-4216-acbc-ee22db52b8b6"Decision Making with Data")\n[![Exploratory Data Analysis](	https://images.credly.com/size/680x680/images/60f3…e798/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/891f1247-1bfb-425a-af60-63837667cfbe"Exploratory Data Analysis")\n[![Quality Methods](https://images.credly.com/size/680x680/images/26b9…9096/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/f384bd74-1202-4b8c-aa7d-74f0937c815a"Quality Methods")\n[![Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression](https://images.credly.com/size/680x680/images/fe43…6_badges_EducationTraining_Learn_AdvAnalytics.png)](https://www.credly.com/earner/earned/badge/5b0712d7-f0e4-4cd9-9ace-830097efaff2"Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression")\n[![SAS Programming 1: Essentials](https://images.credly.com/size/680x680/images/c5d4…56_badges_EducationTraining_Learn_Programming.png)](https://www.credly.com/earner/earned/badge/0135e701-6c8b-484f-8a4b-81003ce99b31"SAS Programming 1: Essentials")\n<!--END_SECTION:badges-->',
            new_readme,
        )

        self.assertNotEqual(with_tags_text_between, new_readme)

class testNotTagsHTML(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_not_tag(self):
        no_tags = return_markdown("no_tags.md")
        self.assertEqual("# badge-readme\nThis is example file", no_tags)

        badges = Credly(FOLDER_HTML+"no_badges.html").get_markdown()
        new_readme = generate_new_readme(badges, no_tags)
        self.assertEqual("# badge-readme\nThis is example file", new_readme)

        self.assertEqual(no_tags, new_readme)

    def test_with_tags_no_text_between(self):
        with_tags_no_text_between = return_markdown("with_tags_no_text_between.md")
        self.assertEqual(
            "# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<!--END_SECTION:badges-->",
            with_tags_no_text_between,
        )

        badges = Credly(FOLDER_HTML+"no_badges.html").get_markdown()
        new_readme = generate_new_readme(badges, with_tags_no_text_between)
        self.assertEqual(
            "# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<!--END_SECTION:badges-->",
            new_readme,
        )

        self.assertEqual(with_tags_no_text_between, new_readme)

    def test_with_tags_text_between(self):
        with_tags_text_between = return_markdown("with_tags_text_between.md")
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<p align="left"><a href=" https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" title=" PYTHON FOR DATA SCIECNCE AND AI "><img src=" https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png " alt=" PYTHON FOR DATA SCIECNCE AND AI "></img></a><a href=" https://www.credly.com/earner/earned/badge/ba4ac412-79a2-4d49-9c0f-b0a1548dae23" title=" Predictive Modeling and Text Mining "><img src=" https://images.credly.com/size/680x680/images/e98b…4112/62056_badges_EducationTraining_Learn_JMP.png " alt="Predictive Modeling and Text Mining"></img></a><a href="https://www.credly.com/earner/earned/badge/8995bdd4-eee7-4160-99b2-28683fb1782c " title=" Statistical Thinking and Problem Solving "><img src=" https://images.credly.com/size/680x680/images/7b88…dc50/62056_badges_EducationTraining_Learn_JMP.png " alt=" Statistical Thinking and Problem Solving "></img></a> <a href=" https://www.credly.com/earner/earned/badge/a333254f-9448-4485-9a3e-08691ad06ea7" title=" Correlation and Regression "><img src=" https://images.credly.com/size/680x680/images/ad66…dcd4/62056_badges_EducationTraining_Learn_JMP.png " alt=" Correlation and Regression "></img></a><a href=" https://www.credly.com/earner/earned/badge/3afac32d-3299-4337-80a3-a4150471c32b " title=" Design of Experiments "><img src=" https://images.credly.com/size/680x680/images/d96b…a128/62056_badges_EducationTraining_Learn_JMP.png " alt=" Design of Experiments "></img></a><a href=" https://www.credly.com/earner/earned/badge/eb253681-509f-4216-acbc-ee22db52b8b6" title=" Decision Making with Data "><img src=" https://images.credly.com/size/680x680/images/d05f…4575/62056_badges_EducationTraining_Learn_JMP.png " alt=" Decision Making with Data "></img></a> <a href=" https://www.credly.com/earner/earned/badge/891f1247-1bfb-425a-af60-63837667cfbe " title=" Exploratory Data Analysis "><img src=" https://images.credly.com/size/680x680/images/60f3…e798/62056_badges_EducationTraining_Learn_JMP.png) " alt=" Exploratory Data Analysis "></img></a><a href=" https://www.credly.com/earner/earned/badge/f384bd74-1202-4b8c-aa7d-74f0937c815a " title=" Quality Methods "><img src=" https://images.credly.com/size/680x680/images/26b9…9096/62056_badges_EducationTraining_Learn_JMP.png " alt=" Quality Methods "></img></a><a href=" https://www.credly.com/earner/earned/badge/5b0712d7-f0e4-4cd9-9ace-830097efaff2" title=" Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression "><img src="https://images.credly.com/size/680x680/images/fe43…6_badges_EducationTraining_Learn_AdvAnalytics.png " alt=" Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression "></img></a><a href="https://www.credly.com/earner/earned/badge/0135e701-6c8b-484f-8a4b-81003ce99b31" title=" SAS Programming 1: Essentials "><img src=" https://images.credly.com/size/680x680/images/c5d4…56_badges_EducationTraining_Learn_Programming.png " alt=" SAS Programming 1: Essentials "></img></a></p> \n<!--END_SECTION:badges-->',
            with_tags_text_between,
        )

        badges = Credly(FOLDER_HTML+"no_badges.html").get_markdown()
        new_readme = generate_new_readme(badges, with_tags_text_between)
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<p align="left"><a href=" https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" title=" PYTHON FOR DATA SCIECNCE AND AI "><img src=" https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png " alt=" PYTHON FOR DATA SCIECNCE AND AI "></img></a><a href=" https://www.credly.com/earner/earned/badge/ba4ac412-79a2-4d49-9c0f-b0a1548dae23" title=" Predictive Modeling and Text Mining "><img src=" https://images.credly.com/size/680x680/images/e98b…4112/62056_badges_EducationTraining_Learn_JMP.png " alt="Predictive Modeling and Text Mining"></img></a><a href="https://www.credly.com/earner/earned/badge/8995bdd4-eee7-4160-99b2-28683fb1782c " title=" Statistical Thinking and Problem Solving "><img src=" https://images.credly.com/size/680x680/images/7b88…dc50/62056_badges_EducationTraining_Learn_JMP.png " alt=" Statistical Thinking and Problem Solving "></img></a> <a href=" https://www.credly.com/earner/earned/badge/a333254f-9448-4485-9a3e-08691ad06ea7" title=" Correlation and Regression "><img src=" https://images.credly.com/size/680x680/images/ad66…dcd4/62056_badges_EducationTraining_Learn_JMP.png " alt=" Correlation and Regression "></img></a><a href=" https://www.credly.com/earner/earned/badge/3afac32d-3299-4337-80a3-a4150471c32b " title=" Design of Experiments "><img src=" https://images.credly.com/size/680x680/images/d96b…a128/62056_badges_EducationTraining_Learn_JMP.png " alt=" Design of Experiments "></img></a><a href=" https://www.credly.com/earner/earned/badge/eb253681-509f-4216-acbc-ee22db52b8b6" title=" Decision Making with Data "><img src=" https://images.credly.com/size/680x680/images/d05f…4575/62056_badges_EducationTraining_Learn_JMP.png " alt=" Decision Making with Data "></img></a> <a href=" https://www.credly.com/earner/earned/badge/891f1247-1bfb-425a-af60-63837667cfbe " title=" Exploratory Data Analysis "><img src=" https://images.credly.com/size/680x680/images/60f3…e798/62056_badges_EducationTraining_Learn_JMP.png) " alt=" Exploratory Data Analysis "></img></a><a href=" https://www.credly.com/earner/earned/badge/f384bd74-1202-4b8c-aa7d-74f0937c815a " title=" Quality Methods "><img src=" https://images.credly.com/size/680x680/images/26b9…9096/62056_badges_EducationTraining_Learn_JMP.png " alt=" Quality Methods "></img></a><a href=" https://www.credly.com/earner/earned/badge/5b0712d7-f0e4-4cd9-9ace-830097efaff2" title=" Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression "><img src="https://images.credly.com/size/680x680/images/fe43…6_badges_EducationTraining_Learn_AdvAnalytics.png " alt=" Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression "></img></a><a href="https://www.credly.com/earner/earned/badge/0135e701-6c8b-484f-8a4b-81003ce99b31" title=" SAS Programming 1: Essentials "><img src=" https://images.credly.com/size/680x680/images/c5d4…56_badges_EducationTraining_Learn_Programming.png " alt=" SAS Programming 1: Essentials "></img></a></p> \n<!--END_SECTION:badges-->',
            new_readme,
        )

        self.assertEqual(with_tags_text_between, new_readme)

class testNoChangesHTML(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_not_changes(self):
        no_changes = return_markdown("no_changes_happy_day.md")
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n\n[![ PYTHON FOR DATA SCIECNCE AND AI](https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png)](https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" PYTHON FOR DATA SCIECNCE AND AI")\n[![Predictive Modeling and Text Mining](https://images.credly.com/size/680x680/images/e98b…4112/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/ba4ac412-79a2-4d49-9c0f-b0a1548dae23"Predictive Modeling and Text Mining")\n[![Statistical Thinking and Problem Solving](https://images.credly.com/size/680x680/images/7b88…dc50/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/8995bdd4-eee7-4160-99b2-28683fb1782c"Statistical Thinking and Problem Solving")\n[![Correlation and Regression](https://images.credly.com/size/680x680/images/ad66…dcd4/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/a333254f-9448-4485-9a3e-08691ad06ea7"Correlation and Regression")\n[![Design of Experiments](https://images.credly.com/size/680x680/images/d96b…a128/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/3afac32d-3299-4337-80a3-a4150471c32b"Design of Experiments")\n[![Decision Making with Data](	https://images.credly.com/size/680x680/images/d05f…4575/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/eb253681-509f-4216-acbc-ee22db52b8b6"Decision Making with Data")\n[![Exploratory Data Analysis](	https://images.credly.com/size/680x680/images/60f3…e798/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/891f1247-1bfb-425a-af60-63837667cfbe"Exploratory Data Analysis")\n[![Quality Methods](https://images.credly.com/size/680x680/images/26b9…9096/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/f384bd74-1202-4b8c-aa7d-74f0937c815a"Quality Methods")\n[![Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression](https://images.credly.com/size/680x680/images/fe43…6_badges_EducationTraining_Learn_AdvAnalytics.png)](https://www.credly.com/earner/earned/badge/5b0712d7-f0e4-4cd9-9ace-830097efaff2"Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression")\n[![SAS Programming 1: Essentials](https://images.credly.com/size/680x680/images/c5d4…56_badges_EducationTraining_Learn_Programming.png)](https://www.credly.com/earner/earned/badge/0135e701-6c8b-484f-8a4b-81003ce99b31"SAS Programming 1: Essentials")\n<!--END_SECTION:badges-->',
            no_changes,
        )

        badges = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        new_readme = generate_new_readme(badges, no_changes)
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n\n[![ PYTHON FOR DATA SCIECNCE AND AI](https://images.credly.com/size/680x680/images/0571…d61b7/Python_for_Data_Sci_and_AI_Foundational.png)](https://www.credly.com/earner/earned/badge/53e8e71a-c1b7-4aab-b0af-6db447da9547" PYTHON FOR DATA SCIECNCE AND AI")\n[![Predictive Modeling and Text Mining](https://images.credly.com/size/680x680/images/e98b…4112/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/ba4ac412-79a2-4d49-9c0f-b0a1548dae23"Predictive Modeling and Text Mining")\n[![Statistical Thinking and Problem Solving](https://images.credly.com/size/680x680/images/7b88…dc50/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/8995bdd4-eee7-4160-99b2-28683fb1782c"Statistical Thinking and Problem Solving")\n[![Correlation and Regression](https://images.credly.com/size/680x680/images/ad66…dcd4/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/a333254f-9448-4485-9a3e-08691ad06ea7"Correlation and Regression")\n[![Design of Experiments](https://images.credly.com/size/680x680/images/d96b…a128/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/3afac32d-3299-4337-80a3-a4150471c32b"Design of Experiments")\n[![Decision Making with Data](	https://images.credly.com/size/680x680/images/d05f…4575/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/eb253681-509f-4216-acbc-ee22db52b8b6"Decision Making with Data")\n[![Exploratory Data Analysis](	https://images.credly.com/size/680x680/images/60f3…e798/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/891f1247-1bfb-425a-af60-63837667cfbe"Exploratory Data Analysis")\n[![Quality Methods](https://images.credly.com/size/680x680/images/26b9…9096/62056_badges_EducationTraining_Learn_JMP.png)](https://www.credly.com/earner/earned/badge/f384bd74-1202-4b8c-aa7d-74f0937c815a"Quality Methods")\n[![Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression](https://images.credly.com/size/680x680/images/fe43…6_badges_EducationTraining_Learn_AdvAnalytics.png)](https://www.credly.com/earner/earned/badge/5b0712d7-f0e4-4cd9-9ace-830097efaff2"Statistics 1: Introduction to ANOVA, Regression, and Logistic Regression")\n[![SAS Programming 1: Essentials](https://images.credly.com/size/680x680/images/c5d4…56_badges_EducationTraining_Learn_Programming.png)](https://www.credly.com/earner/earned/badge/0135e701-6c8b-484f-8a4b-81003ce99b31"SAS Programming 1: Essentials")\n<!--END_SECTION:badges-->',
            new_readme,
        )

        self.assertEqual(no_changes, new_readme)
