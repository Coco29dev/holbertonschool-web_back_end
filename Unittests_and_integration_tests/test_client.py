#!/usr/bin/env python3
"""Unit tests for client module."""
import unittest
from unittest.mock import patch, PropertyMock
from utils import memoize
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test that org returns the expected payload."""
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, expected_payload)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected URL."""
        org_name = "google"
        expected_url = "https://api.github.com/orgs/google/repos"

        client = GithubOrgClient(org_name)
        result = client._public_repos_url

        self.assertEqual(result, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected list of repos."""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/test/repos"
            )

            client = GithubOrgClient("test")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the expected boolean."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration tests."""
        cls.get_patcher = patch('client.get_json')
        cls.mock_get_json = cls.get_patcher.start()

        cls.mock_get_json.side_effect = [
            {"repos_url": "https://api.github.com/orgs/test/repos"},
            [
                {"name": "repo1", "license": {"key": "my_license"}},
                {"name": "repo2", "license": {"key": "other_license"}},
                {"name": "repo3", "license": {"key": "my_license"}},
            ],
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class for integration tests."""
        cls.get_patcher.stop()

    @parameterized.expand([
        ("test", ["repo1", "repo2", "repo3"]),
    ])
    def test_public_repos_integration(self, org_name, expected_repos):
        """Test that public_repos returns the expected list of repos."""
        client = GithubOrgClient(org_name)
        result = client.public_repos()
        self.assertEqual(result, expected_repos)


if __name__ == "__main__":
    unittest.main()
