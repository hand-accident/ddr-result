<script>
    let className;
    export { className as class };
</script>

<div class="c {className}">
    <slot />
</div>

<style lang="postcss" module>
    .c {
        @apply inline-flex items-center justify-center transition duration-200 ease-in-out h-6 leading-6 px-2.5
        border rounded-badge border-current border-opacity-50 bg-transparent text-current;
        width: fit-content;
    }
</style>
