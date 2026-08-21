import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIVATE_REPO_URLS = (
    "https://github.com/oldprize47-SH/stm32-automatic-recycling-system",
    "https://github.com/oldprize47-SH/gaze-tracking-mouse",
)
BANNED_JOINT_STM_IMAGE_SHA256 = "dd4aa32f4d0176c280c04a9bcb019d5a1af8358f8f3613ac0f14beb50cc9211d"
BANNED_JOINT_GAZE_IMAGE_SHA256 = {
    "82830b5bb41da971944711e8198c5ee6cf990b072db19c8769a9de01c85bfba9",
    "b5d767c0e90b08734e657fa48a44b57dd3e315a42270b1a33ce0fc4821261967",
}
BANNED_TEAM_REALSENSE_IMAGE_SHA256 = "28d8419ca8278d520906dce273e04baa148f4f4a520383d112f15c4b0731c40f"


class ProfilePublicationContractTests(unittest.TestCase):
    def test_private_repository_urls_are_not_clickable(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        hrefs = set(re.findall(r'href=["\']([^"\']+)', readme))
        self.assertTrue(set(PRIVATE_REPO_URLS).isdisjoint(hrefs))

    def test_stm_visual_is_an_original_self_contained_overview(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        visual = ROOT / "assets" / "stm32-system-overview.svg"
        self.assertIn("./assets/stm32-system-overview.svg", readme)
        self.assertTrue(visual.is_file())
        svg = visual.read_text(encoding="utf-8")
        self.assertNotRegex(svg, r"(?i)<image\b|href\s*=\s*[\"']https?://")
        self.assertNotEqual(
            hashlib.sha256(visual.read_bytes()).hexdigest(),
            BANNED_JOINT_STM_IMAGE_SHA256,
        )

    def test_realsense_denominator_names_the_vision_lock_subset(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("vision lock이 확인된 실외 비행 6회 중", readme)

    def test_realsense_visual_is_an_original_self_contained_overview(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        visual = ROOT / "assets" / "realsense-system-overview.svg"
        self.assertIn("./assets/realsense-system-overview.svg", readme)
        self.assertTrue(visual.is_file())
        svg = visual.read_text(encoding="utf-8")
        self.assertNotRegex(svg, r"(?i)<image\b|href\s*=\s*[\"']https?://")
        self.assertNotEqual(
            hashlib.sha256(visual.read_bytes()).hexdigest(),
            BANNED_TEAM_REALSENSE_IMAGE_SHA256,
        )

    def test_gaze_visuals_are_original_self_contained_summaries(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        expected = (
            ROOT / "assets" / "gaze-system-overview.svg",
            ROOT / "assets" / "gaze-metric-summary.svg",
        )
        for visual in expected:
            rel = f"./assets/{visual.name}"
            self.assertIn(rel, readme)
            self.assertTrue(visual.is_file())
            svg = visual.read_text(encoding="utf-8")
            self.assertNotRegex(svg, r"(?i)<image\b|href\s*=\s*[\"']https?://")
            self.assertNotIn(hashlib.sha256(visual.read_bytes()).hexdigest(), BANNED_JOINT_GAZE_IMAGE_SHA256)


if __name__ == "__main__":
    unittest.main()
