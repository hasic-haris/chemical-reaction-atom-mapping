""" The 'chemical_reaction_atom_mapping.utilities.multiprocessing' package 'multiprocessing' module. """

from logging import getLogger
from multiprocessing import cpu_count, Pool
from tqdm import tqdm
from typing import Any, Callable, Iterable, List, Optional


class MultiprocessingUtilities:
    """ The multiprocessing utilities class. """

    @staticmethod
    def run(
            processing_procedure: Callable[..., Any],
            primary_input_arguments: Iterable[Any],
            number_of_cpu_cores: int = 1,
            enable_logger: bool = False
    ) -> Optional[List[Any]]:
        """
        Run a processing procedure for each primary input argument.

        :parameter processing_procedure: The processing procedure.
        :parameter primary_input_arguments: The primary input arguments of the processing procedure.
        :parameter number_of_cpu_cores: The number of CPU cores that should be utilized.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The output of the processing procedure for each primary input argument.
        """

        try:
            number_of_cpu_cores = number_of_cpu_cores if 1 <= number_of_cpu_cores <= cpu_count() else 1

            processing_procedure_outputs = list()

            if number_of_cpu_cores == 1:
                for primary_input_argument in primary_input_arguments:
                    processing_procedure_outputs.append(
                        processing_procedure(primary_input_argument)
                    )

            else:
                with Pool(number_of_cpu_cores) as process_pool:
                    for processing_procedure_output in process_pool.map(processing_procedure, primary_input_arguments):
                        processing_procedure_outputs.append(
                            processing_procedure_output
                        )

                    process_pool.close()
                    process_pool.join()

            return processing_procedure_outputs

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MultiprocessingUtilities.run".format(__name__)
                ).exception(exception_handle)

            raise

    @staticmethod
    def run_with_progress_bar(
            processing_procedure: Callable[..., Any],
            primary_input_argument: Iterable[Any],
            number_of_primary_input_arguments: int = None,
            description_message: str = None,
            number_of_cpu_cores: int = 1,
            enable_logger: bool = False,
    ) -> Optional[List[Any]]:
        """
        Run a processing procedure for each primary input argument, and visualize the progress with a progress bar.

        :parameter processing_procedure: The processing procedure.
        :parameter primary_input_argument: The primary input arguments of the processing procedure.
        :parameter number_of_primary_input_arguments: The number of primary input arguments of the processing procedure.
        :parameter description_message: The progress bar description message.
        :parameter number_of_cpu_cores: The number of CPU cores that should be utilized.
        :parameter enable_logger: The indicator whether the logger should be enabled.

        :returns: The output of the processing procedure for each primary input argument.
        """

        try:
            number_of_cpu_cores = number_of_cpu_cores if 1 <= number_of_cpu_cores <= cpu_count() else 1

            processing_procedure_outputs = list()

            if number_of_cpu_cores == 1:
                for input_argument in tqdm(
                    iterable=primary_input_argument,
                    total=number_of_primary_input_arguments,
                    ascii=True,
                    ncols=150,
                    desc="{0} (CPU Cores: 1)".format(
                        description_message if description_message is not None else "Running"
                    )
                ):
                    processing_procedure_outputs.append(
                        processing_procedure(input_argument)
                    )

            else:
                with Pool(number_of_cpu_cores) as process_pool:
                    for processing_procedure_output in tqdm(
                        iterable=process_pool.imap(processing_procedure, primary_input_argument),
                        total=number_of_primary_input_arguments,
                        ascii=True,
                        ncols=150,
                        desc="{0} (CPU Cores: {1})".format(
                            description_message if description_message is not None else "Running",
                            number_of_cpu_cores
                        )
                    ):
                        processing_procedure_outputs.append(
                            processing_procedure_output
                        )

                    process_pool.close()
                    process_pool.join()

            return processing_procedure_outputs

        except Exception as exception_handle:
            if enable_logger:
                getLogger(
                    "{0}.MultiprocessingUtilities.run_with_progress_bar".format(__name__)
                ).exception(exception_handle)

            raise
