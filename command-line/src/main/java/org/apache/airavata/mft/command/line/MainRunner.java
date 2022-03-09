package org.apache.airavata.mft.command.line;

import org.apache.airavata.mft.command.line.sub.s3.S3SubCommand;
import picocli.CommandLine;
import picocli.CommandLine.Command;

@Command(name = "checksum", mixinStandardHelpOptions = true, version = "checksum 4.0",
        description = "Prints the checksum (SHA-256 by default) of a file to STDOUT.",
        subcommands = {S3SubCommand.class})
class MainRunner {

    public static void main(String... args) {
        int exitCode = new CommandLine(new MainRunner())
                .execute(args);
        System.exit(exitCode);
    }
}
