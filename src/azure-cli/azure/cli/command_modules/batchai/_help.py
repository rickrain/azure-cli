# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['batchai'] = """
type: group
short-summary: Manage Batch AI resources.
"""

helps['batchai cluster'] = """
type: group
short-summary: Commands to manage clusters.
"""

helps['batchai cluster auto-scale'] = """
type: command
short-summary: Set auto-scale parameters for a cluster.
examples:
  - name: Make a cluster to auto scale between 0 and 10 nodes depending on number of queued and running jobs.
    text: az batchai cluster auto-scale -g MyResourceGroup -w MyWorkspace -n MyCluster --min 0 --max 10
"""

helps['batchai cluster create'] = """
type: command
short-summary: Create a cluster.
examples:
  - name: Create a single node GPU cluster with default image and auto-storage account.
    text: |
        az batchai cluster create -g MyResourceGroup -w MyWorkspace -n MyCluster \\
            -s Standard_NC6 -t 1 --use-auto-storage --generate-ssh-keys
  - name: Create a cluster with a setup command which installs unzip on every node, the command output will be stored on auto storage account Azure File Share.
    text: |
        az batchai cluster create -g MyResourceGroup -w MyWorkspace -n MyCluster \\
            --use-auto-storage \\
            -s Standard_NC6 -t 1 -k id_rsa.pub \\
            --setup-task 'apt update; apt install unzip -y' \\
            --setup-task-output '$AZ_BATCHAI_MOUNT_ROOT/autoafs'
  - name: Create a cluster providing all parameters manually.
    text: |
        az batchai cluster create -g MyResourceGroup -w MyWorkspace -n MyCluster \\
            -i UbuntuLTS -s Standard_NC6 --vm-priority lowpriority \\
            --min 0 --target 1 --max 10 \\
            --storage-account-name MyStorageAccount \\
            --nfs MyNfsToMount --afs-name MyAzureFileShareToMount \\
            --bfs-name MyBlobContainerNameToMount \\
            -u AdminUserName -k id_rsa.pub -p ImpossibleToGuessPassword
  - name: Create a cluster using a configuration file.
    text: >
        az batchai cluster create -g MyResourceGroup -w MyWorkspace -n MyCluster -f cluster.json

"""

helps['batchai cluster delete'] = """
type: command
short-summary: Delete a cluster.
examples:
  - name: Delete a cluster and wait for deletion to be completed.
    text: az batchai cluster delete -g MyResourceGroup -w MyWorkspace -n MyCluster
  - name: Send a delete command for a cluster and do not wait for deletion to be completed.
    text: az batchai cluster delete -g MyResourceGroup -w MyWorkspace -n MyCluster --no-wait
  - name: Delete cluster without asking for confirmation (for non-interactive scenarios).
    text: az batchai cluster delete -g MyResourceGroup -w MyWorkspace -n MyCluster -y
"""

helps['batchai cluster file'] = """
type: group
short-summary: Commands to work with files generated by node setup task.
"""

helps['batchai cluster file list'] = """
type: command
short-summary: List files generated by the cluster's node setup task.
long-summary: List files generated by the cluster's node setup task under $AZ_BATCHAI_STDOUTERR_DIR path. This functionality is available only if the node setup task output directory is located on mounted Azure File Share or Azure Blob Container.
examples:
  - name: List names and sizes of files and directories inside of $AZ_BATCHAI_STDOUTERR_DIR.
    text: |
        az batchai cluster file list -g MyResourceGroup -w MyWorkspace -c MyCluster -o table
  - name: List names, sizes and download URLs for files and directories inside of $AZ_BATCHAI_STDOUTERR_DIR.
    text: |
        az batchai cluster file list -g MyResourceGroup -w MyWorkspace -c MyCluster
  - name: List names, sizes and download URLs for files and directories inside of $AZ_BATCHAI_STDOUTERR_DIR/folder/subfolder.
    text: |
        az batchai cluster file list -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            -p folder/subfolder
  - name: List names, sizes and download URLs for files and directories inside of $AZ_BATCHAI_STDOUTERR_DIR making download URLs to remain valid for one hour.
    text: |
        az batchai cluster file list -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            --expiry 60
"""

helps['batchai cluster list'] = """
type: command
short-summary: List clusters.
examples:
  - name: List all clusters in a workspace.
    text: az batchai cluster list -g MyResourceGroup -w MyWorkspace -o table
"""

helps['batchai cluster node'] = """
type: group
short-summary: Commands to work with cluster nodes.
"""

helps['batchai cluster node exec'] = """
type: command
short-summary: Executes a command line on a cluster's node with optional ports forwarding.
examples:
  - name: Report a snapshot of the current processes.
    text: |
        az batchai cluster node exec -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            -n tvm-xxx --exec "ps axu"
  - name: Report a GPU information for a node.
    text: |
        az batchai cluster node exec -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            -n tvm-xxx --exec "nvidia-smi"
  - name: Forward local 9000 to port 9001 on the node.
    text: |
        az batchai cluster node exec -g MyResourceGroup -w MyWorkspace -c MyCluster \\
            -n tvm-xxx -L 9000:localhost:9001
"""

helps['batchai cluster node list'] = """
type: command
short-summary: List remote login information for cluster's nodes.
long-summary: "List remote login information for cluster nodes. You can ssh to a particular node using the provided public IP address and the port number.\nE.g. `ssh <admin user name>@<public ip> -p <node's SSH port number>`"
examples:
  - name: List remote login information for a cluster.
    text: az batchai cluster node list -g MyResourceGroup -w MyWorkspace -c MyCluster -o table
"""

helps['batchai cluster resize'] = """
type: command
short-summary: Resize a cluster.
examples:
  - name: Resize a cluster to zero size to stop paying for it.
    text: az batchai cluster resize -g MyResourceGroup -w MyWorkspace -n MyCluster -t 0
  - name: Resize a cluster to have 10 nodes.
    text: az batchai cluster resize -g MyResourceGroup -w MyWorkspace -n MyCluster -t 10
"""

helps['batchai cluster show'] = """
type: command
short-summary: Show information about a cluster.
examples:
  - name: Show full information about a cluster.
    text: az batchai cluster show -g MyResourceGroup -w MyWorkspace -n MyCluster
  - name: Show cluster's summary.
    text: az batchai cluster show -g MyResourceGroup -w MyWorkspace -n MyCluster -o table
"""

helps['batchai experiment'] = """
type: group
short-summary: Commands to manage experiments.
"""

helps['batchai experiment create'] = """
type: command
short-summary: Create an experiment.
examples:
  - name: Create an experiment.
    text: az batchai experiment create -g MyResourceGroup -w MyWorkspace -n MyExperiment
"""

helps['batchai experiment delete'] = """
type: command
short-summary: Delete an experiment.
examples:
  - name: Delete an experiment. All running jobs will be terminated.
    text: az batchai experiment delete -g MyResourceGroup -w MyWorkspace -n MyExperiment
  - name: Delete an experiment without asking for confirmation (for non-interactive scenarios).
    text: az batchai experiment delete -g MyResourceGroup -w MyWorkspace -n MyExperiment -y
  - name: Request an experiment deletion without waiting for job to be deleted.
    text: az batchai experiment delete -g MyResourceGroup -w MyWorkspace -n MyExperiment --no-wait
"""

helps['batchai experiment list'] = """
type: command
short-summary: List experiments.
examples:
  - name: List experiments.
    text: az batchai experiment list -g MyResourceGroup -w MyWorkspace -o table
"""

helps['batchai experiment show'] = """
type: command
short-summary: Show information about an experiment.
examples:
  - name: Show information about an experiment.
    text: az batchai experiment show -g MyResourceGroup -w MyWorkspace -n MyExperiment -o table
"""

helps['batchai file-server'] = """
type: group
short-summary: Commands to manage file servers.
"""

helps['batchai file-server create'] = """
type: command
short-summary: Create a file server.
examples:
  - name: Create a NFS file server using a configuration file.
    text: az batchai file-server create -g MyResourceGroup -w MyWorkspace -n MyNFS -f nfs.json
  - name: Create a NFS manually providing parameters.
    text: |
        az batchai file-server create -g MyResourceGroup -w MyWorkspace -n MyNFS \\
            -s Standard_D14 --disk-count 4 --disk-size 512 \\
            --storage-sku Premium_LRS --caching-type readonly \\
            -u $USER -k ~/.ssh/id_rsa.pub
"""

# helps['batchai file-server delete'] = """
# # type: command
# short-summary: Delete a file server.
# examples:
#   - name: Delete file server and wait for deletion to be completed.
#     text: az batchai file-server delete -g MyResourceGroup -w MyWorkspace -n MyNFS
#   - name: Delete file server without asking for confirmation (for non-interactive scenarios).
#     text: az batchai file-server delete -g MyResourceGroup -w MyWorkspace -n MyNFS -y
#   - name: Request file server deletion without waiting for deletion to be completed.
#     text: az batchai file-server delete -g MyResourceGroup -w MyWorkspace -n MyNFS --no-wait
# """

helps['batchai file-server list'] = """
type: command
short-summary: List file servers.
examples:
  - name: List all file servers in the given workspace.
    text: az batchai file-server list -g MyResourceGroup -w MyWorkspace -o table
"""

# helps['batchai file-server show'] = """
# # type: command
# short-summary: Show information about a file server.
# examples:
#   - name: Show full information about a file server.
#     text: az batchai file-server show -g MyResourceGroup -w MyWorkspace -n MyNFS
#   - name: Show file server summary.
#     text: az batchai file-server show -g MyResourceGroup -w MyWorkspace -n MyNFS -o table
#
# """

helps['batchai job'] = """
type: group
short-summary: Commands to manage jobs.
"""

helps['batchai job create'] = """
type: command
short-summary: Create a job.
examples:
  - name: Create a job to run on a cluster in the same resource group.
    text: |
        az batchai job create -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob \\
            -c MyCluster -f job.json
  - name: Create a job to run on a cluster in a different workspace.
    text: |
        az batchai job create -g MyJobResourceGroup -w MyJobWorkspace -e MyExperiment -n MyJob \\
            -f job.json \\
            -c "/subscriptions/00000000-0000-0000-0000-000000000000/\\
            resourceGroups/MyClusterResourceGroup/\\
            providers/Microsoft.BatchAI/workspaces/MyClusterWorkspace/clusters/MyCluster"
  - name: Create a job. (autogenerated)
    text: |
        az batchai job create --cluster "/subscriptions/00000000-0000-0000-0000-000000000000/\\
            resourceGroups/MyClusterResourceGroup/\\
            providers/Microsoft.BatchAI/workspaces/MyClusterWorkspace/clusters/MyCluster" --config-file job.json --experiment MyExperiment --name MyJob --resource-group MyJobResourceGroup --storage-account-name MyStorageAccount --workspace MyJobWorkspace
    crafted: true
"""

helps['batchai job delete'] = """
type: command
short-summary: Delete a job.
examples:
  - name: Delete a job. The job will be terminated if it's currently running.
    text: az batchai job delete -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob
  - name: Delete a job without asking for confirmation (for non-interactive scenarios).
    text: az batchai job delete -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob -y
  - name: Request job deletion without waiting for job to be deleted.
    text: az batchai job delete -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob --no-wait
"""

helps['batchai job file'] = """
type: group
short-summary: Commands to list and stream files in job's output directories.
"""

helps['batchai job file list'] = """
type: command
short-summary: List job's output files in a directory with given id.
long-summary: List job's output files in a directory with given id if the output directory is located on mounted Azure File Share or Blob Container.
examples:
  - name: List files in the standard output directory of the job.
    text: |
        az batchai job file list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob
  - name: List files in the standard output directory of the job. Generates output in a table format.
    text: |
        az batchai job file list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob -o table
  - name: List files in a folder 'MyFolder/MySubfolder' of an output directory with id 'MODELS'.
    text: |
        az batchai job file list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            -d MODELS -p MyFolder/MySubfolder
  - name: List files in the standard output directory of the job making download URLs to remain valid for 15 minutes.
    text: |
        az batchai job file list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            --expiry 15
"""

helps['batchai job file stream'] = """
type: command
short-summary: Stream the content of a file (similar to 'tail -f').
long-summary: Waits for the job to create the given file and starts streaming it similar to 'tail -f' command. The command completes when the job finished execution.
examples:
  - name: Stream standard output file of the job.
    text: |
        az batchai job file stream -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            -f stdout.txt
  - name: Stream a file 'log.txt' from a folder 'logs' of an output directory with id 'OUTPUTS'.
    text: |
        az batchai job file stream -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            -d OUTPUTS -p logs -f log.txt
"""

helps['batchai job list'] = """
type: command
short-summary: List jobs.
examples:
  - name: List jobs.
    text: az batchai job list -g MyResourceGroup -w MyWorkspace -e MyExperiment -o table
"""

helps['batchai job node'] = """
type: group
short-summary: Commands to work with nodes which executed a job.
"""

helps['batchai job node exec'] = """
type: command
short-summary: Executes a command line on a cluster's node used to execute the job with optional ports forwarding.
examples:
  - name: Report a GPU state for a job's node.
    text: |
        az batchai job node exec -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            --exec "nvidia-smi"
  - name: Report a snapshot of the current processes.
    text: |
        az batchai job node exec -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            --exec "ps aux"
  - name: Forward local 9000 to port 9001 on the given node.
    text: |
        az batchai job node exec -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob \\
            -n tvm-xxx -L 9000:localhost:9001
"""

helps['batchai job node list'] = """
type: command
short-summary: List remote login information for nodes which executed the job.
long-summary: "List remote login information for currently existing (not deallocated) nodes on which the job was executed. You can ssh to a particular node using the provided public IP address and the port number.\nE.g. `ssh <admin user name>@<public ip> -p <node's SSH port number>`"
examples:
  - name: List remote login information for a job nodes.
    text: az batchai job node list -g MyResourceGroup -w MyWorkspace -e MyExperiment -j MyJob -o table
"""

helps['batchai job show'] = """
type: command
short-summary: Show information about a job.
examples:
  - name: Show full information about a job.
    text: az batchai job show -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob
  - name: Show job's summary.
    text: az batchai job show -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob -o table
"""

helps['batchai job terminate'] = """
type: command
short-summary: Terminate a job.
examples:
  - name: Terminate a job and wait for the job to be terminated.
    text: az batchai job terminate -g MyResourceGroup -w MyWorkspace -e MyExperiment -n MyJob
  - name: Terminate a job without asking for confirmation (for non-interactive scenarios).
    text: az batchai job terminate -g MyResourceGroup  -w MyWorkspace -e MyExperiment -n MyJob -y
  - name: Request job termination without waiting for the job to be terminated.
    text: |
        az batchai job terminate -g MyResourceGroup -e MyExperiment -w MyWorkspace -n MyJob \\
            --no-wait
"""

helps['batchai job wait'] = """
type: command
short-summary: Waits for specified job completion and setups the exit code to the job's exit code.
examples:
  - name: Wait for the job completion.
    text: |
        az batchai job wait -g MyResourceGroup -w MyWorkspace -n MyJob
"""

helps['batchai list-usages'] = """
type: command
short-summary: Gets the current usage information as well as limits for Batch AI resources for given location.
examples:
  - name: Get information for eastus location.
    text: az batchai list-usages -l eastus -o table
  - name: Gets the current usage information as well as limits for Batch AI resources for given location. (autogenerated)
    text: az batchai list-usages --location eastus --subscription MySubscription
    crafted: true
"""

helps['batchai workspace'] = """
type: group
short-summary: Commands to manage workspaces.
"""

helps['batchai workspace create'] = """
type: command
short-summary: Create a workspace.
examples:
  - name: Create a workspace in East US region.
    text: az batchai workspace create -g MyResourceGroup -n MyWorkspace -l eastus
"""

helps['batchai workspace delete'] = """
type: command
short-summary: Delete a workspace.
examples:
  - name: Delete a workspace.
    text: az batchai workspace delete -g MyResourceGroup -n MyWorkspace
"""

helps['batchai workspace list'] = """
type: command
short-summary: List workspaces.
examples:
  - name: List all workspaces under the current subscription.
    text: az batchai workspace list -o table
  - name: List workspaces in the given resource group.
    text: az batchai workspace list -g MyResourceGroup -o table
"""

helps['batchai workspace show'] = """
type: command
short-summary: Show information about a workspace.
examples:
  - name: Show information about a workspace.
    text: az batchai workspace show -g MyResourceGroup -n MyWorkspace -o table
"""
