import pytest

import demistomock as demisto

integration_params = {
    'url': 'https://localhost',
    'APItoken': 'token',
    'username': 'test',
    'password': '1234!',
    'query': 'status=Open'
}


@pytest.fixture(autouse=True)
def set_params(mocker):
    mocker.patch.object(demisto, 'params', return_value=integration_params)


def test_issue_query_command_no_issues(mocker):
    """
    Given
    - Jira issue query command

    When
    - Sending HTTP request and getting no issues from the query

    Then
    - Verify no error message is thrown to the user
    """
    from JiraV2 import issue_query_command
    mocker.patch('JiraV2.run_query', return_value={})
    human_readable, _, _ = issue_query_command('status=Open AND labels=lies')
    assert 'No issues matched the query' in human_readable


def test_fetch_incidents_no_incidents(mocker):
    """
    Given
    - Jira fetch incidents command

    When
    - Sending HTTP request and getting no issues from the query

    Then
    - Verify no incidents are returned
    """
    from JiraV2 import fetch_incidents
    mocker.patch('JiraV2.run_query', return_value={})
    incidents = fetch_incidents('status=Open AND labels=lies', id_offset=1)
    assert incidents == []
